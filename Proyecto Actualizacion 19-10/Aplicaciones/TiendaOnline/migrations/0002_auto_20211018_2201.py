# Generated by Django 3.2.6 on 2021-10-19 04:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('TiendaOnline', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='accesorio',
            old_name='descripcion',
            new_name='descripciona',
        ),
        migrations.RenameField(
            model_name='accesorio',
            old_name='foto',
            new_name='fotoa',
        ),
        migrations.RenameField(
            model_name='accesorio',
            old_name='marca',
            new_name='marcaa',
        ),
        migrations.RenameField(
            model_name='accesorio',
            old_name='nombre',
            new_name='nombrea',
        ),
        migrations.RenameField(
            model_name='accesorio',
            old_name='precio',
            new_name='precioa',
        ),
        migrations.RenameField(
            model_name='accesorio',
            old_name='tipo',
            new_name='tipoa',
        ),
    ]
