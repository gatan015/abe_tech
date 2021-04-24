from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.Home, name='pegawai'),
    path('tambah-pegawai', views.tambahPegawai, name='tambah-pegawai'),
    path('profil/<str:pk>/', views.profil, name='profil'),
    path('update/<str:pk>/', views.updatePegawai, name='update'),
    path('delete/<str:pk>/', views.deletePegawai, name='delete'),
]
