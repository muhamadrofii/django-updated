# Generated by Django 5.1.4 on 2024-12-14 10:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accountsapp', '0008_profilechild'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profilechild',
            name='nama_lengkap',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='profilechild',
            name='pendidikan',
            field=models.CharField(blank=True, choices=[('belum sekolah', 'Belum Sekolah'), ('tk_a', 'TK A'), ('tk_b', 'TK B'), ('sd_1', 'SD Kelas 1'), ('sd_2', 'SD Kelas 2'), ('sd_3', 'SD Kelas 3'), ('sd_4', 'SD Kelas 4'), ('sd_5', 'SD Kelas 5'), ('sd_6', 'SD Kelas 6')], max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='profilechild',
            name='umur',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]
