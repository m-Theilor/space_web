from django.db import models
from datetime import datetime

class Fotografia(models.Model):

    OPCOES_CATEGORIA = [
        ('NEBULOSA','Nebulosa'),
        ('ENTRELA','Estrela'),
        ('GALÁXIA','Galáxia'),
        ('PLANETA','Planeta'),
    ]

    nome = models.CharField('Nome', max_length=100, null=False, blank=False)
    legenda = models.CharField('Legenda', max_length=150, null=False, blank=False)
    categoria = models.CharField('Categoria', choices = OPCOES_CATEGORIA, max_length=100, default = '')
    descricao = models.TextField('Descricao', null=False, blank=False)
    foto= models.ImageField(upload_to='fotos/%Y/%m/%d', blank=True)
    publicada = models.BooleanField('Publicada', default=False)
    data_fotografia = models.DateTimeField('Data de Fotografia', default=datetime.now, blank=False)


    def __str__(self):
        return self.nome

