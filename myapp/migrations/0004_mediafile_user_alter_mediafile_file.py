# Generated by Django 5.1.2 on 2024-11-05 14:48

import django.db.models.deletion
import myapp.models
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_folder_alter_mediafile_folder'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='mediafile',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='mediafile',
            name='file',
            field=models.FileField(upload_to=myapp.models.user_directory_path),
        ),
    ]
