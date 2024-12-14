# Generated by Django 5.1.3 on 2024-12-10 13:49

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accountsapp', '0007_profileparent_avatar'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProfileChild',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama_lengkap', models.CharField(max_length=200)),
                ('umur', models.PositiveIntegerField()),
                ('pendidikan', models.CharField(choices=[('belum sekolah', 'Belum Sekolah'), ('tk_a', 'TK A'), ('tk_b', 'TK B'), ('sd_1', 'SD Kelas 1'), ('sd_2', 'SD Kelas 2'), ('sd_3', 'SD Kelas 3'), ('sd_4', 'SD Kelas 4'), ('sd_5', 'SD Kelas 5'), ('sd_6', 'SD Kelas 6')], max_length=20)),
                ('bidang_minat', models.CharField(blank=True, choices=[('olahraga', 'Olahraga'), ('berhitung', 'Berhitung')], max_length=200, null=True)),
                ('parent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='children', to='accountsapp.profileparent')),
            ],
        ),
    ]