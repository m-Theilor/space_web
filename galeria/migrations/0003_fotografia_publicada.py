# Generated by Django 5.1.4 on 2025-01-06 18:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('galeria', '0002_fotografia_categoria_alter_fotografia_foto'),
    ]

    operations = [
        migrations.AddField(
            model_name='fotografia',
            name='publicada',
            field=models.BooleanField(default=False, verbose_name='Publicada'),
        ),
    ]
