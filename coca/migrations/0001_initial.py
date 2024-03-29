# Generated by Django 5.0.1 on 2024-03-06 13:52

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Appareil',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=50)),
                ('type', models.CharField(blank=True, max_length=50)),
                ('cote', models.DecimalField(decimal_places=2, max_digits=5)),
                ('puissance', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=5, null=True)),
            ],
            options={
                'verbose_name': 'Appareil',
                'verbose_name_plural': 'Appareils',
                'db_table': '',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Devis',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now_add=True)),
                ('energie_T', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
            ],
            options={
                'verbose_name': 'Devis',
                'verbose_name_plural': 'Deviss',
                'db_table': '',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Devis_Appareil',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantite', models.IntegerField()),
                ('numHours', models.IntegerField(blank=True, default=0, null=True)),
                ('power', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('energie_T', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('appareil', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='coca.appareil')),
                ('devis', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='coca.devis')),
            ],
            options={
                'verbose_name': 'Devis_Appareil',
                'verbose_name_plural': 'Devis_Appareils',
                'db_table': '',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='InformationsInternaute',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=100)),
                ('prenom', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=50, unique=True)),
                ('addres', models.CharField(max_length=50)),
                ('telephone', models.CharField(max_length=20)),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='internaute', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='devis',
            name='internaute_temp',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='coca.informationsinternaute'),
        ),
    ]
