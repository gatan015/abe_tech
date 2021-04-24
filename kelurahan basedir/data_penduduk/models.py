from django.db import models

# Create your models here.
class skawin(models.Model):
    nama = models.CharField(max_length=50)
    keterangan = models.TextField()

    def __str__(self):
        return self.nama

class jkel(models.Model):
    nama = models.CharField(max_length=50)
    keterangan = models.TextField()

    def __str__(self):
        return self.nama

class kagama(models.Model):
    nama = models.CharField(max_length=50)
    keterangan = models.TextField()

    def __str__(self):
        return self.nama

class didik(models.Model):
    nama = models.CharField(max_length=50)
    keterangan = models.TextField()

    def __str__(self):
        return self.nama

class kerja(models.Model):
    nama = models.CharField(max_length=50)
    keterangan = models.TextField()

    def __str__(self):
        return self.nama

class stinggal(models.Model):
    nama = models.CharField(max_length=50)
    keterangan = models.TextField()

    def __str__(self):
        return self.nama

class goldarah(models.Model):
    nama = models.CharField(max_length=50)
    keterangan = models.TextField()

    def __str__(self):
        return self.nama

class Penduduk(models.Model):
    no_kk = models.IntegerField(null=True)
    nik = models.IntegerField(null=True)
    nama = models.CharField(max_length=50)
    tempat_lahir = models.CharField(max_length=50)
    tanggal_lahir = models.DateField(max_length=50)
    gol_darah = models.ForeignKey(goldarah, on_delete=models.CASCADE, null=True)
    status_kawin = models.ForeignKey(skawin, on_delete=models.CASCADE, null=True)
    jenis_kelamin = models.ForeignKey(jkel, on_delete=models.CASCADE, null=True)
    agama = models.ForeignKey(kagama, on_delete=models.CASCADE, null=True)
    alamat = models.CharField(max_length=50)
    rt = models.IntegerField(null=True)
    rw = models.IntegerField(null=True)
    kelurahan = models.CharField(max_length=50)
    pendidikan = models.ForeignKey(didik, on_delete=models.CASCADE, null=True)
    pekerjaan = models.ForeignKey(kerja, on_delete=models.CASCADE, null=True)
    status_tinggal = models.ForeignKey(stinggal, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.nama
