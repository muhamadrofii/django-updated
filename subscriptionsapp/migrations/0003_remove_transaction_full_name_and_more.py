# Generated by Django 5.1.3 on 2024-12-12 15:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('subscriptionsapp', '0002_alter_transaction_plan'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='transaction',
            name='full_name',
        ),
        migrations.RemoveField(
            model_name='transaction',
            name='profile',
        ),
    ]
