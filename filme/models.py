import dataclasses

from django.db import models
from django.utils import timezone

# Create your models here.

LISTA_CATEGORIAS = (
    ('ANALISES','Análises'),
    ('APRESENTACAO','Apresentação'),
    ('PROGRAMACAO', 'Programação'),
    ('COMEDIA', 'Comedia'),
    ('DRAMA', 'Drama'),
    ('TERROR', 'Terror'),
    ('SUSPENSE', 'Suspense'),
    ('FICCAO', 'Ficção'),
    ('ANIMACAO', 'Animação'),
    ('ACAO', 'Ação'),
    ('AVENTURA', 'Aventura'),
    ('OUTROS', 'Outros'),
)

#Criar o filme
class Filme(models.Model):
    thumb = models.ImageField(upload_to='thumb_filmes')
    titulo = models.CharField(max_length=100)
    descricao = models.TextField(max_length=1000)
    categoria = models.CharField(max_length=15, choices=LISTA_CATEGORIAS)
    visualisacoes = models.IntegerField(default=0)
    data_criacao = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.titulo

#Criar o episodio
class Episodio (models.Model):
    filme = models.ForeignKey('Filme', related_name='episodios', on_delete=models.CASCADE)
    titulo = models.CharField(max_length=100)
    video = models.URLField(max_length=100)

    def __str__(self):
        return self.filme.titulo + ' - ' + self.titulo


#Criar o usuario
