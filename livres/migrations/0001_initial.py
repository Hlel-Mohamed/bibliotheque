# Generated by Django 5.1.3 on 2024-11-21 12:28

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Livre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titre', models.CharField(max_length=200)),
                ('auteur', models.CharField(max_length=200)),
                ('date_publication', models.DateField()),
                ('disponible', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Emprunt',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom_emprunteur', models.CharField(max_length=200)),
                ('date_emprunt', models.DateField(default=django.utils.timezone.now)),
                ('livre', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='livres.livre')),
            ],
        ),
    ]
