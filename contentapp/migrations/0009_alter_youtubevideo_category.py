# Generated by Django 5.1.4 on 2024-12-15 15:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contentapp', '0008_alter_choice_text'),
    ]

    operations = [
        migrations.AlterField(
            model_name='youtubevideo',
            name='category',
            field=models.CharField(blank=True, choices=[('Post Test', 'Post Test'), ('Post Parent', 'Post Parent'), ('Post Kids', 'Post Kids'), ('Parenting Dasar', 'Parenting Dasar'), ('Ide Bekal Sekolah', 'Ide Bekal Sekolah'), ('Ruang Baca', 'Ruang Baca'), ('Animal', 'Animal'), ('ABC & 123', 'ABC & 123'), ('Warna & Bentuk', 'Warna & Bentuk'), ('Science', 'Science')], max_length=255, null=True),
        ),
    ]
