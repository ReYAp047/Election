from django.db import models
from django.db.models.deletion import CASCADE
from cloudinary.models import CloudinaryField
# from cloudinary.models import CloudinaryField
# Create your models here.

class Images(models.Model):
    Titre = models.CharField(max_length=50, blank=False)
    Image = CloudinaryField('Images', blank=True)
    def __str__(self):
        return self.Titre

class Condidat(models.Model):
    Images = models.ManyToManyField(Images, blank=False)
    Nom_condidat = models.CharField(max_length=512,blank=False)
    Cin = models.IntegerField(blank=False)
    Date_Naissance = models.DateField(blank=False)
    Titre = models.CharField(max_length=4000,blank=False)
    Objectif = models.CharField(max_length=4000,blank=False)
    Description = models.CharField(max_length=4000,blank=False)

    Nb_vote = models.IntegerField(blank=True, editable=False, default=0)
    def __str__(self):
        return self.Nom_condidat