from django.db import models


# Create your models here.

class Usuarios(models.Model):
    Id_user = models.CharField(max_length=10)
    nombre_user = models.CharField(max_length=30)
    apellido_user = models.CharField(max_length=30)
    email_user = models.CharField(max_length=60)
    escolaridad_user = models.CharField(max_length=30)
    filiacion_user = models.CharField(max_length=100)
