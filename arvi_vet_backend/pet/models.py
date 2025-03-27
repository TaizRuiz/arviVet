from django.db import models


class Pet(models.Model):
    nombre = models.CharField(max_length=100)
    