# Generated by Django 2.2.3 on 2022-10-12 16:35

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Inicio', '0006_remove_nota_color'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nota',
            name='actualizado',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]