from django.db import models

# Create your models here.
class Compagnie(models.Model):
    nom = models.CharField(max_length=255)
    logo=models.CharField(max_length=255)

    class Meta:
        ordering = ['nom']

    def __str__(self):
        return self.nom
    
class Trajet(models.Model):
    depart=models.CharField(max_length=255)
    arrive=models.CharField(max_length=255)
    class Meta:
        ordering=['depart']
    def __str__(self):
        return self.depart  
        

class Vol(models.Model):
    prix = models.FloatField()
    datevol=models.CharField(max_length=255)
    heure=models.CharField(max_length=255)
    Compagnies = models.ManyToManyField(Compagnie)
    Trajets = models.ForeignKey(Trajet, on_delete=models.CASCADE)

    class Meta:
        ordering = ['heure']

    def __str__(self):
        return self.prix+''+self.datevol+' '+self.Compagnies