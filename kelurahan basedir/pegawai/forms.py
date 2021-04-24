from django.forms import ModelForm
from .models import Pegawai
from django import forms

class PegawaiForm(ModelForm):
    class Meta:
        model = Pegawai
        fields = "__all__"

        widgets = {
            'nama' : forms.TextInput({ 'class' : 'form-control' }),
            'nip' : forms.TextInput({ 'class' : 'form-control' }),
            'status' : forms.Select({ 'class' : 'form-control' }),
            'jabatan' : forms.Select({ 'class' : 'form-control' }),
            'jenis_kelamin' : forms.Select({ 'class' : 'form-control' }),
            'telpon' : forms.TextInput({ 'class' : 'form-control' }),
            'email' : forms.TextInput({ 'class' : 'form-control' }),
            'note' : forms.TextInput({ 'class' : 'form-control' }),
        }