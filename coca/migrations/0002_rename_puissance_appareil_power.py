# Generated by Django 5.0.1 on 2024-03-13 12:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('coca', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='appareil',
            old_name='puissance',
            new_name='power',
        ),
    ]
