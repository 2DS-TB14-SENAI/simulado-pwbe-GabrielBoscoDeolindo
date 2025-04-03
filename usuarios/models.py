from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class Usuario(AbstractUser):
    telefone = models.CharField(max_length=15, blank=True, null=True)

    def __str__(self):
        return self.username