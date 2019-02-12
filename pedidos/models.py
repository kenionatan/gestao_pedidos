from django.db import models
from clientes.models import Cliente
from usuarios.models import Usuario


class Pedido(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, default=None)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, default=None)
