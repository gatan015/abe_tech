# Generated by Django 2.2 on 2021-04-23 01:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pegawai', '0004_auto_20210423_0819'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pegawai',
            name='nip',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]