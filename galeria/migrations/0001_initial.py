# Generated by Django 5.1.4 on 2025-01-06 13:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Fotografia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100, verbose_name='Nome')),
                ('legenda', models.CharField(max_length=150, verbose_name='Legenda')),
                ('descricao', models.TextField(verbose_name='Descricao')),
                ('foto', models.CharField(max_length=150, verbose_name='Foto')),
            ],
        ),
    ]
