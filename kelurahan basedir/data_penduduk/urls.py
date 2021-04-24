from django.contrib import admin
from django.urls import path, include
from . import views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('', views.home ,name='index'),
    path('tentang/', views.tentang , name='tentang'),
    path('kontak/', views.kontak , name='kontak'),
    path('penduduk/', views.penduduk, name='data_penduduk'),
    path('penduduk/tambah-penduduk/', views.tambahPenduduk, name='tambahPenduduk'),
    path('penduduk/ubah/<int:id_penduduk>', views.ubah_penduduk, name='ubah_penduduk'),
    path('penduduk/hapus/<int:id_penduduk>', views.hapus_penduduk, name='hapus_penduduk'),
    path('penduduk/profil/<int:id_penduduk>', views.profilPenduduk, name='profilPenduduk'),
    path('masuk', LoginView.as_view(), name='masuk'),
    path('keluar', LogoutView.as_view(next_page='index'), name='keluar'),
    path('signup', views.signup, name='signup'),
]
