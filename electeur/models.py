from django.db import models
from django.db.models.deletion import CASCADE
# Create your models here.
class Electeur(models.Model):
    Cin = models.IntegerField(blank=False)
    Nom_electeur = models.CharField(max_length=512,blank=False)
    Date_Naissance = models.DateField(blank=False)
    Titre = models.CharField(max_length=4000,blank=False)

    Voter = models.BooleanField(editable=False, default=False)
    def __str__(self):
        return self.Nom_Action