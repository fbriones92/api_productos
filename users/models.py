from django.contrib.auth.models import AbstractUser
from django.db import models

class Usuario(AbstractUser):
    # Agrega campos personalizados
    fecha_nacimiento = models.DateField(null=True, blank=True)
    rol_id = models.IntegerField(blank=True)
    
    def __str__(self):
        return self.username