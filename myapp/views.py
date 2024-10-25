from django.shortcuts import render, redirect
from .forms import MediaFileForm
from .models import MediaFile




def upload_file(request):
    if request.method == 'POST':
        form = MediaFileForm(request.POST, request.FILES)
        if form.is_valid():
            #on envoie le fichier dans le dossier media
            form.save()
            return redirect('upload_file')
    else:
        form = MediaFileForm()

    # Récupérer tous les fichiers
    files = MediaFile.objects.all()
    return render(request, 'myapp/home.html', {'form': form, 'files': files})