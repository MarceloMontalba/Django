# Generated by Django 3.2 on 2022-07-29 03:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('peliculas', '0008_pelicula_generos'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pelicula',
            name='generos',
        ),
        migrations.AddField(
            model_name='pelicula',
            name='genero',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='pelicula',
            name='descripcion',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.DeleteModel(
            name='Genero',
        ),
    ]