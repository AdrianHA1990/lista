# Generated by Django 4.1.6 on 2023-02-15 21:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Area',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estado', models.BooleanField(default=True)),
                ('fecha_reg', models.DateTimeField(auto_now_add=True)),
                ('fecha_act', models.DateTimeField(auto_now=True)),
                ('nom_area', models.CharField(max_length=150, verbose_name='Area')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Usuario')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Estudio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estado', models.BooleanField(default=True)),
                ('fecha_reg', models.DateTimeField(auto_now_add=True)),
                ('fecha_act', models.DateTimeField(auto_now=True)),
                ('nom_est', models.CharField(max_length=150, verbose_name='Area')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Usuario')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='personal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estado', models.BooleanField(default=True)),
                ('fecha_reg', models.DateTimeField(auto_now_add=True)),
                ('fecha_act', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=100, verbose_name='Nombre')),
                ('ap', models.CharField(max_length=100, verbose_name='Apellido Paterno')),
                ('am', models.CharField(max_length=100, verbose_name='Apellido Materno')),
                ('foto', models.ImageField(blank=True, null=True, upload_to='imagenes/', verbose_name='Foto')),
                ('Carrera', models.CharField(choices=[('Sistemas', 'Sistemas'), ('Contabilidad', 'Contabilidad'), ('Derecho', 'Derecho'), ('Adminsitracion', 'Administracion')], max_length=100, verbose_name='Carrera')),
                ('area', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='personal.area', verbose_name='Area')),
                ('estudio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='personal.estudio', verbose_name='Estudio')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Usuario')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
