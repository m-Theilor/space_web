# Generated by Django 5.1.4 on 2025-01-06 18:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('galeria', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='fotografia',
            name='categoria',
            field=models.CharField(choices=[('NEBULOSA', 'Nebulosa'), ('ENTRELA', 'Estrela'), ('GALÁXIA', 'Galáxia'), ('PLANETA', 'Planeta')], default='', max_length=100, verbose_name='Categoria'),
        ),
        migrations.AlterField(
            model_name='fotografia',
            name='foto',
            field=models.CharField(max_length=100, verbose_name='Foto'),
        ),
    ]
