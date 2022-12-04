from django.db import models

# Create your models here.
class Compagnie(models.Model):
    nom = models.CharField(max_length=255)
    logo=models.CharField(max_length=255)

    class Meta:
        ordering = ['nom']

    def __str__(self):
        return self.nom

class Article(models.Model):
    headline = models.CharField(max_length=100)
    Compagnies = models.ManyToManyField(Compagnie)

    class Meta:
        ordering = ['attdevol']

    def __str__(self