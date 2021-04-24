from django.contrib import admin
from data_penduduk.models import *
from pegawai.models import *

# Register your models here.
class PageAdmin(admin.ModelAdmin):
    list_display = ['no_kk', 'nik', 'nama', 'jenis_kelamin', 'alamat', 'rt', 'rw']
    search_fields = ['no_kk', 'nik', 'nama']
    list_filter = ('status_tinggal', 'jenis_kelamin')
    list_per_page = 8

class PagePegawai(admin.ModelAdmin):
    list_display = ['nama', 'nip', 'jabatan', 'telpon', 'email']
    search_fields = ['nama', 'nip']
    list_filter = ('jabatan',)
    list_per_page = 5

admin.site.register(Penduduk, PageAdmin)
admin.site.register(skawin)
admin.site.register(jkel)
admin.site.register(kagama)
admin.site.register(didik)
admin.site.register(kerja)
admin.site.register(stinggal)
admin.site.register(goldarah)

admin.site.register(Pegawai, PagePegawai)
admin.site.register(Jabatan)