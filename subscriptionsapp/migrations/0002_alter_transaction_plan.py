# Generated by Django 5.1.3 on 2024-12-12 02:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subscriptionsapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='plan',
            field=models.CharField(blank=True, choices=[('trial', 'Trial Plan'), ('basic', 'Basic Plan'), ('premium', 'Premium Plan'), ('ultimate', 'Ultimate Plan')], max_length=20, null=True),
        ),
    ]
