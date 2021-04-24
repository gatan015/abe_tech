from django.forms import ModelForm
from django import forms
from .models import *

class FormPenduduk(ModelForm):
    class Meta:
        model = Penduduk
        fields = '__all__'

        widgets = {
            'no_kk' : forms.NumberInput({ 'class' : 'form-control' }),
            'nik' : forms.NumberInput({ 'class' : 'form-control' }),
            'nama' : forms.TextInput({ 'class' : 'form-control' }),
            'tempat_lahir' : forms.TextInput({ 'class' : 'form-control' }),
            'tanggal_lahir' : forms.DateInput(attrs = { 'type' : 'date' }),
            'gol_darah' : forms.Select({ 'class' : 'form-control' }),
            'status_kawin' : forms.Select({ 'class' : 'form-control' }),
            'jenis_kelamin' : forms.Select({ 'class' : 'form-control' }),
            'agama' : forms.Select({ 'class' : 'form-control' }),
            'alamat' : forms.TextInput({ 'class' : 'form-control' }),
            'rt' : forms.NumberInput({ 'class' : 'form-control' }),
            'rw' : forms.NumberInput({ 'class' : 'form-control' }),
            'kelurahan' : forms.TextInput({ 'class' : 'form-control' }),
            'pendidikan' : forms.Select({ 'class' : 'form-control' }),
            'pekerjaan' : forms.Select({ 'class' : 'form-control' }),
            'status_tinggal' : forms.Select({ 'class' : 'form-control' }),
        }
