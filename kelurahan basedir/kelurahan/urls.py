from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('data_penduduk.urls'), name='penduduk'),
    path('pegawai/', include('pegawai.urls'), name='pegawai'),
]
