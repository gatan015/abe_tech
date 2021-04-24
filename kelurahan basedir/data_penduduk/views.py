from django.shortcuts import render, redirect
from .models import *
from .forms import FormPenduduk
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.contrib.auth.forms import UserCreationForm
from django.db.models import Count
from .filters import PendudukFilter

# Create your views here.
def tentang(request):
    return render(request, 'tentang.html')

def kontak(request):
    return render(request, 'kontak.html')

def home(request):
    return render(request, 'index.html')

@login_required(login_url=settings.LOGIN_URL)
def penduduk(request):
    penduduk = Penduduk.objects.all()
    total_penduduk = penduduk.count()
    laki = Penduduk.objects.filter(jenis_kelamin__nama='Laki-laki').count()
    perempuan = Penduduk.objects.filter(jenis_kelamin__nama='Perempuan').count()

    myFilter = PendudukFilter(request.GET, queryset=penduduk)
    penduduk = myFilter.qs
    
    konteks = {
        'penduduk' : penduduk,
        'total_penduduk':total_penduduk,
        'laki':laki,
        'perempuan':perempuan,
        'myFilter':myFilter,
    }
    return render(request, 'data_penduduk/penduduk.html', konteks)

@login_required(login_url=settings.LOGIN_URL)
def profilPenduduk(request, id_penduduk):
    penduduk = Penduduk.objects.get(id=id_penduduk)

    context = {'penduduk':penduduk,}
    return render(request, 'data_penduduk/profil-penduduk.html', context)

@login_required(login_url=settings.LOGIN_URL)
def tambahPenduduk(request):
    if request.POST:
        form = FormPenduduk(request.POST)
        if form.is_valid():
            form.save()
            form = FormPenduduk()
            pesan = 'Data Berhasil Ditambahkan!'

            konteks = {
                'form' : form,
                'pesan' : pesan,
            }

            return render(request, 'data_penduduk/tambah-penduduk.html', konteks)

    else:
        form = FormPenduduk()
        konteks = {
            'form' : form,
        }

        return render(request, 'data_penduduk/tambah-penduduk.html', konteks)

@login_required(login_url=settings.LOGIN_URL)
def ubah_penduduk(request, id_penduduk):
    penduduk = Penduduk.objects.get(id=id_penduduk)
    template = 'data_penduduk/ubah-penduduk.html'
    if request.POST:
        form = FormPenduduk(request.POST, instance=penduduk)
        if form.is_valid():
            form.save()
            return redirect('profilPenduduk', id_penduduk=id_penduduk)
    else:
        form = FormPenduduk(instance=penduduk)
        konteks = {
            'form' : form,
            'penduduk' : penduduk,
        }
        return render(request, template, konteks)

@login_required(login_url=settings.LOGIN_URL)
def hapus_penduduk(request, id_penduduk):
    penduduk = Penduduk.objects.filter(id=id_penduduk)
    penduduk.delete()

    return redirect('data_penduduk')

@login_required(login_url=settings.LOGIN_URL)
def signup(request):
    if request.POST:
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'User berhasil dibuat!')
            return redirect('signup')
        else:
            message.error(request, 'terjadi Kesalahan!')
            return redirect('signup')
    else:
        form = UserCreationForm()
        konteks = {
            'form' : form
        }

    return render(request, 'data_penduduk/signup.html', konteks)