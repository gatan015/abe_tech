from django.db import models

# Create your models here.
class Jabatan(models.Model):
    nama = models.CharField(max_length=100)
    keterangan = models.TextField()

    def __str__(self):
        return self.nama

class Pegawai(models.Model):
    STATUS = (
            ('ASN', 'ASN'),
            ('PHL', 'PHL'),
            )

    JKEL = (
            ('Laki-laki', 'Laki-laki'),
            ('Perempuan', 'Perempuan'),
            )

    nama = models.CharField(max_length=100)
    nip = models.CharField(max_length=20, null=True, blank=True)
    status = models.CharField(max_length=200, null=True, choices=STATUS)
    jabatan = models.ForeignKey(Jabatan, on_delete=models.CASCADE, null=True, blank=True)
    jenis_kelamin = models.CharField(max_length=200, null=True, choices=JKEL)
    telpon = models.CharField(max_length=20, null=True, blank=True)
    email = models.CharField(max_length=30, null=True, blank=True)
    note = models.CharField(max_length=1000, null=True, blank=True)

    def __str__(self):
        return self.nama