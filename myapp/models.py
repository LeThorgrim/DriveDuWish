# myapp/models.py
from django.db import models
import os

class Folder(models.Model):
    name = models.CharField(max_length=100)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_full_path(self):
        """
        Retourne le chemin complet du dossier à partir du répertoire 'media'
        """
        if self.parent:
            return os.path.join(self.parent.get_full_path(), self.name)
        return self.name

class MediaFile(models.Model):
    title = models.CharField(max_length=100)
    file = models.FileField(upload_to='uploads/')
    folder = models.ForeignKey(Folder, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.title
