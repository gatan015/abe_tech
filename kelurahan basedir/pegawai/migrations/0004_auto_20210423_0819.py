# Generated by Django 2.2 on 2021-04-23 01:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pegawai', '0003_auto_20210423_0817'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pegawai',
            name='telpon',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]