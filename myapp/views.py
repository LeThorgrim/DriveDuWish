import os
import shutil
from django.conf import settings
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .forms import MediaFileForm, FolderForm
from .models import MediaFile, Folder
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.db.models import Count
from collections import Counter
from django.db.models import Q # Pour les requêtes de recherche


#Création de dossier et fichiers/Upload de fichiers
def upload_file(request):
    if request.method == 'POST':
        file_form = MediaFileForm(request.POST, request.FILES)
        folder_form = FolderForm(request.POST)
        
        user_folder_path = os.path.join(settings.MEDIA_ROOT, request.user.username)
        os.makedirs(user_folder_path, exist_ok=True)

    if 'add_file' in request.POST and file_form.is_valid():
            file_instance = file_form.save(commit=False)
            file_instance.user = request.user  # Associate the file with the logged-in user
            file_instance.save()
            return redirect('upload_file')

    if 'add_folder' in request.POST and folder_form.is_valid():
        folder_instance = folder_form.save(commit=False)
        folder_instance.user = request.user  # Associer le dossier à l'utilisateur connecté
        folder_instance.save()
        # Créer un dossier physique pour le dossier
        os.makedirs(os.path.join(user_folder_path, folder_instance.get_full_path()), exist_ok=True)
        return redirect('upload_file')

    else:
        file_form = MediaFileForm()
        folder_form = FolderForm()

    # ici on récupère les fichiers et dossiers de l'utilisateur et uniquement ceux de l'utilisateur
    user_folders = Folder.objects.filter(parent__isnull=True, user=request.user)
    user_files = MediaFile.objects.filter(user=request.user)

    all_files = MediaFile.objects.all()
    file_types = [os.path.splitext(file.file.name)[1].lower() for file in all_files]
    file_type_counts =dict(Counter(file_types))
    
    
    

      

    return render(request, 'myapp/home.html', {
        'file_form': file_form,
        'folder_form': folder_form,
        'folders': folders,
        'files': files,
        'folder_count':folder_count,
        'folder_file_count':folder_file_counts,
        'folder_file_counts_json':folder_file_counts_json,
        'file_type_counts':json.dumps(file_type_counts),
    })

def delete_file(request, file_id):
    file_instance = get_object_or_404(MediaFile, id=file_id)
    file_path = os.path.join(settings.MEDIA_ROOT, file_instance.file.name)
    
    if os.path.exists(file_path):
        os.remove(file_path)
    
    file_instance.delete()
    return redirect('upload_file')

def delete_folder(request, folder_id):
    folder_instance = get_object_or_404(Folder, id=folder_id)
    folder_path = os.path.join(settings.MEDIA_ROOT, folder_instance.get_full_path())
    
    # Supprimer tous les fichiers dans le dossier
    files = MediaFile.objects.filter(folder=folder_instance)
    for file in files:
        file_path = os.path.join(settings.MEDIA_ROOT, file.file.name)
        if os.path.exists(file_path):
            os.remove(file_path)
        file.delete()
    
    # Supprimer tous les sous-dossiers
    subfolders = Folder.objects.filter(parent=folder_instance)
    for subfolder in subfolders:
        delete_folder(request, subfolder.id)
    
    # Supprimer le dossier physique et son contenu
    if os.path.exists(folder_path):
        shutil.rmtree(folder_path)
    
    folder_instance.delete()
    return redirect('upload_file')

def create_physical_folder(folder_instance):
    # Crée un dossier physique dans le dossier uploads de media
    folder_path = os.path.join(settings.MEDIA_ROOT, folder_instance.get_full_path())
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

def view_folder(request, folder_id):
    folder_instance = get_object_or_404(Folder, id=folder_id, user=request.user)
    files = MediaFile.objects.filter(folder=folder_instance, user=request.user)
    subfolders = Folder.objects.filter(parent=folder_instance, user=request.user)
    
    return render(request, 'myapp/folder_view.html', {
        'folder': folder_instance,
        'files': files,
        'subfolders': subfolders,
    })


#recherche de fichier
def search_files(request):
    query = request.GET.get('query', '')
    # Recherche tous les fichiers et dossiers de l'utilisateur
    files = MediaFile.objects.filter(user=request.user).filter(
        Q(title__icontains=query) |
        Q(folder__name__icontains=query)
    )
    folders = Folder.objects.filter(user=request.user).filter(
        Q(name__icontains=query)
    )

    return render(request, 'myapp/home.html', {
        'file_form': MediaFileForm(),
        'folder_form': FolderForm(),
        'folders': folders,
        'files': files,
        'query': query,
    })

    
def mon_drive(request):
    # Ne récupérer que les fichiers qui ne sont pas dans des sous-dossiers
    files = MediaFile.objects.filter(user=request.user, folder__isnull=True)
    folders = Folder.objects.filter(user=request.user)

    return render(request, 'myapp/home.html', {
        'file_form': MediaFileForm(),
        'folder_form': FolderForm(),
        'folders': folders,
        'files': files,
    })
