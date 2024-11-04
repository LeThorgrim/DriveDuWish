from django.urls import path
from . import views

urlpatterns = [
    path('', views.upload_file, name='upload_file'),
    path('delete_file/<int:file_id>/', views.delete_file, name='delete_file'),
    path('delete_folder/<int:folder_id>/', views.delete_folder, name='delete_folder'),
    path('view_folder/<int:folder_id>/', views.view_folder, name='view_folder'),
    
]