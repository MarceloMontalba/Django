# Generated by Django 3.2 on 2022-07-25 15:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pelicula',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50)),
                ('descripcion', models.TextField()),
                ('director', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='generos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('genero', models.CharField(max_length=20)),
                ('pelicula', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='peliculas.pelicula')),
            ],
        ),
    ]