# Generated by Django 3.2.6 on 2021-10-20 00:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TiendaOnline', '0002_auto_20211018_2201'),
    ]

    operations = [
        migrations.CreateModel(
            name='imgMarcas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('foto', models.CharField(max_length=30)),
                ('creacion', models.DateField(auto_now_add=True)),
                ('actualizacion', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
