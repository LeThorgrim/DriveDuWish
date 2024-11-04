import os
import json
import shutil
from django.conf import settings
from django.shortcuts import render, redirect, get_object_or_404
from .forms import MediaFileForm, FolderForm
from .models import MediaFile, Folder
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages

def upload_file(request):
    if request.method == 'POST':
        file_form = MediaFileForm(request.POST, request.FILES)
        folder_form = FolderForm(request.POST)
        
        if 'add_file' in request.POST and file_form.is_valid():
            file_instance = file_form.save(commit=False)
            # Mettre le fichier dans le bon dossier s'il est sélectionné
            if file_instance.folder:
                folder_path = file_instance.folder.get_full_path()
                file_instance.file.name = os.path.join(folder_path, file_instance.file.name)
            file_instance.save()
            return redirect('upload_file')

        if 'add_folder' in request.POST and folder_form.is_valid():
            new_folder = folder_form.save()
            create_physical_folder(new_folder)  # Crée le dossier physique
            return redirect('upload_file')

    else:
        file_form = MediaFileForm()
        folder_form = FolderForm()

    folders = Folder.objects.filter(parent__isnull=True)  # Afficher uniquement les dossiers racine
    files = MediaFile.objects.filter(folder__isnull=True)  # Afficher uniquement les fichiers sans dossier
    
    
    #Statistiques
    folder_count = Folder.objects.count()
    folder_file_counts = []
    for folder in Folder.objects.all():
        folder_file_counts.append({
            'folder_name': folder.name,
            'file_count': MediaFile.objects.filter(folder=folder).count()
        })
        folder_file_counts_json=json.dumps(folder_file_counts)

    return render(request, 'myapp/home.html', {
        'file_form': file_form,
        'folder_form': folder_form,
        'folders': folders,
        'files': files,
        'folder_count':folder_count,
        'folder_file_count':folder_file_counts,
        'folder_file_counts_json':folder_file_counts_json
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



