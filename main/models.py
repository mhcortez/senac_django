from django.db import models

# Create your models here.
class ALuno(models.Model):
    nome = models.CharField(max_length=100)
    telefone = models.CharField(max_length=100)
    email = models.EmailField()
    data_nascimento = models.DateField()
    descricao = models.TextField()

    def __str__(self):
        return self.nome

    