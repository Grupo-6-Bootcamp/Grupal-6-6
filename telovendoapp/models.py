from django.db import models

# Create your models here.
class Proveedores(models.Model):
    nombre = models.CharField(max_length=50, blank=False, null=True)
    rut = models.CharField(max_length=12, blank=False)
    direccion = models.CharField(max_length=50, blank=False, null=True)
    telefono = models.CharField(max_length=12, blank=False, null=True)
    email = models.EmailField(max_length=50, blank=False, null=True)