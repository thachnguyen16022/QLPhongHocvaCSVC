# Generated by Django 5.0 on 2024-01-16 06:58

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Buoi_Hoc',
            fields=[
                ('id_buoihoc', models.AutoField(primary_key=True, serialize=False)),
                ('ten_buoihoc', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Loai_CSVC',
            fields=[
                ('id_tencsvc', models.AutoField(primary_key=True, serialize=False)),
                ('ten_loaicsvc', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Phong_base',
            fields=[
                ('id_phongbase', models.AutoField(primary_key=True, serialize=False)),
                ('toa', models.CharField(max_length=10)),
                ('tang', models.IntegerField()),
                ('phongg', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='phong',
            fields=[
                ('id_phong', models.AutoField(primary_key=True, serialize=False)),
                ('luong_nguoi', models.IntegerField()),
                ('muc_dich', models.CharField(max_length=100)),
                ('tg_bd', models.DateField(blank=True, null=True)),
                ('tg_kt', models.DateField(blank=True, null=True)),
                ('lop_hoc', models.CharField(max_length=50)),
                ('nguoi_dat', models.CharField(max_length=100)),
                ('id_buoihoc', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='home.buoi_hoc')),
                ('id_phongbase', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='home.phong_base')),
            ],
        ),
        migrations.CreateModel(
            name='CSVC',
            fields=[
                ('id_csvc', models.AutoField(primary_key=True, serialize=False)),
                ('so_luong', models.IntegerField()),
                ('id_tencsvc', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='home.loai_csvc')),
                ('id_phongbase', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='home.phong_base')),
            ],
        ),
    ]