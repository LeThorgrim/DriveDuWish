from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_view, name='login'),
    path('login/', views.login_view, name='login'), #doublon mais utile
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register_view, name='register'),
    path('delete/', views.delete_view, name='delete'),
]