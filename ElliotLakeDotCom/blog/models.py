from django.db import models

# Create your models here.


class Book(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100000)
    imagename = models.CharField(max_length=100)

