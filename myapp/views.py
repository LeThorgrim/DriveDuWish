import os
import shutil
from django.conf import settings
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .forms import MediaFileForm, FolderForm
from .models import MediaFile, Folder

def upload_file(request):
    if request.method == 'POST':
        file_form = MediaFileForm(request.POST, request.FILES)
        folder_form = FolderForm(request.POST)
        
        user_folder_path = os.path.join(settings.MEDIA_ROOT, request.user.username)
        os.makedirs(user_folder_path, exist_ok=True)

        if 'add_file' in request.POST and file_form.is_valid():
            file_instance = file_form.save(commit=False)
            file_instance.user = request.user  # Associer le fichier à l'utilisateur connecté
            # Si le fichier est ajouté dans un dossier
            if file_instance.folder:
                folder_path = file_instance.folder.get_full_path()
                file_instance.file.name = os.path.join(request.user.username, folder_path, file_instance.file.name)
            else:
                file_instance.file.name = os.path.join(request.user.username, file_instance.file.name)
            file_instance.save()
            return redirect('upload_file')

        if 'add_folder' in request.POST and folder_form.is_valid():
            folder_instance = folder_form.save(commit=False)
            folder_instance.save()
            # Créer un dossier physique pour le dossier
            os.makedirs(os.path.join(user_folder_path, folder_instance.get_full_path()), exist_ok=True)
            return redirect('upload_file')

    else:
        file_form = MediaFileForm()
        folder_form = FolderForm()

    # ici on récupère les fichiers et dossiers de l'utilisateur et uniquement ceux de l'utilisateur
    user_folders = Folder.objects.filter(parent__isnull=True)
    user_files = MediaFile.objects.filter(folder__isnull=True)

    return render(request, 'myapp/home.html', {
        'file_form': file_form,
        'folder_form': folder_form,
        'folders': user_folders,
        'files': user_files,
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
    folder_instance = get_object_or_404(Folder, id=folder_id)
    files = MediaFile.objects.filter(folder=folder_instance)
    subfolders = Folder.objects.filter(parent=folder_instance)
    
    return render(request, 'myapp/folder_view.html', {
        'folder': folder_instance,
        'files': files,
        'subfolders': subfolders,
    })