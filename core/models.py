from django.db import models
from jsonfield import JSONField


class Meta(models.Model):
    choices = (('C', 'Check'),
               ('T', 'Texto'))

    descricao = models.CharField(max_length=120)
    tipo_validacao = models.CharField(max_length=1, choices=choices)
    peso = models.IntegerField()

    def __str__(self) -> str:
        return self.descricao

    class Meta:
        ordering = ['id']


class Analista(models.Model):
    matricula = models.IntegerField()
    nome = models.CharField(max_length=200)
    data_ultima_avaliacao = models.DateTimeField(null=True)

    def __str__(self) -> str:
        return self.nome

    class Meta:
        ordering = ['nome']


class Avaliacao(models.Model):
    analista = models.ForeignKey('Analista', on_delete=models.CASCADE)
    dados_avaliacao = JSONField()
    resultado = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
