#! -*- coding:utf8 -*-

from django.db import models

class Artigo(models.Model):
	class Meta:
		verbose_name = 'artigo'
		ordering = ['-publicacao']
	titulo = models.CharField(max_length=100, verbose_name='titulo')
	conteudo = models.TextField(verbose_name='conteúdo')
	publicacao = models.DateTimeField(verbose_name='publicação', auto_now_add=True)