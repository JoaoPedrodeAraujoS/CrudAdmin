from django.db import models

# Create your models here.

class Pessoa(models.Model):
	nome = models.CharField(max_length = 100)
	data_nascimento = models.DateField()
	telefone = models.CharField(max_length = 16)
	cpf = models.CharField(max_length = 14)
	RG = models.CharField(max_length = 9)
	endereco = models.CharField(max_length = 200)
	complemento = models.TextField(max_length = 200, blank = True, null = True)
	cep = models.CharField(max_length = 11)
	email = models.CharField(max_length = 100)
	esta_negativado = models.BooleanField(blank = True, null = True)

	def __str__(self):
		return self.nome	