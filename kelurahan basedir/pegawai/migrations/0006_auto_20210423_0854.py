# Generated by Django 2.2 on 2021-04-23 01:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pegawai', '0005_auto_20210423_0820'),
    ]

    operations = [
        migrations.AddField(
            model_name='pegawai',
            name='jenis_kelamin',
            field=models.CharField(choices=[('Laki-laki', 'Laki-laki'), ('Perempuan', 'Perempuan')], max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='pegawai',
            name='note',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='pegawai',
            name='status',
            field=models.CharField(choices=[('Asn', 'Asn'), ('PHL', 'PHL')], max_length=200, null=True),
        ),
    ]