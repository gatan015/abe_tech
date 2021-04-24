from django.shortcuts import render, redirect
from .models import *
from .forms import PegawaiForm
from django.contrib.auth.decorators import login_required
from django.conf import settings

# Create your views here.
@login_required(login_url=settings.LOGIN_URL)
def Home(request):
    pegawai = Pegawai.objects.all()
    total_pegawai = pegawai.count()
    ASN = pegawai.filter(status='ASN').count()
    PHL = pegawai.filter(status='PHL').count()

    context = {'pegawai' : pegawai,'total_pegawai':total_pegawai, 'ASN':ASN, 'PHL':PHL}
    return render(request, 'pegawai/index.html', context)

@login_required(login_url=settings.LOGIN_URL)
def profil(request, pk):
    profil = Pegawai.objects.get(id=pk)

    context = {'profil':profil,}
    return render(request, 'pegawai/profil-pegawai.html', context)

@login_required(login_url=settings.LOGIN_URL)
def tambahPegawai(request):
    if request.method == 'POST':
        form = PegawaiForm(request.POST)
        if form.is_valid():
            form.save()
            form = PegawaiForm()
            pesan = 'Data Berhasil Ditambahkan!'
            
            context = {'form':form, 'pesan':pesan,}
            return render(request, 'pegawai/tambah-pegawai.html', context)

    else:
        form = PegawaiForm()
        context = {'form':form,}
        return render(request, 'pegawai/tambah-pegawai.html', context)

@login_required(login_url=settings.LOGIN_URL)
def updatePegawai(request, pk):
    pegawai = Pegawai.objects.get(id=pk)
    template = 'pegawai/ubah-pegawai.html'
    if request.POST:
        form = PegawaiForm(request.POST, instance=pegawai)
        if form.is_valid():
            form.save()
            return redirect('profil', pk=pk)
    else:
        form = PegawaiForm(instance=pegawai)
        konteks = {
            'form' : form,
            'pegawai' : pegawai,
        }
        return render(request, template, konteks)

@login_required(login_url=settings.LOGIN_URL)
def deletePegawai(request,pk):
    penduduk = Pegawai.objects.filter(id=pk)
    penduduk.delete()

    return redirect('pegawai')