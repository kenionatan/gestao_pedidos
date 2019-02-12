from django.db import models

class Usuario(models.Model):
    nome_usuario = models.CharField(max_length=50)
    email_usuario = models.CharField(max_length=100)
    senha_usuario = models.CharField(max_length=50)

    def __str__(self):
        return self.nome_usuario
