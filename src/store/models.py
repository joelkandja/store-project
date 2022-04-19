from django.db import models

# Create your models here.

class Produit(models.Model):
    nom = models.CharField(max_length=128)
    prix = models.FloatField(default=0.0)
    quantity = models.IntegerField(default=0)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to="produits", blank=True, null=True)
    
    def __str__(self) :
        return self.nom