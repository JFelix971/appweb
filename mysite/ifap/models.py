from django.db import models

# Create your models here.

class CLASSE(models.Model):
    classe = models.CharField(max_length=100,unique=True)

class ORDRE(models.Model):
    ordre = models.CharField(max_length=100,unique=True)

class FAMILLE(models.Model):
    famille = models.CharField(max_length=100,unique=True)

class ANIMAL(models.Model):
    nom_scientifique = models.CharField(max_length=100,unique=True)
    nom_commun = models.CharField(max_length=100,unique=True)
    classe = models.ForeignKey(CLASSE,on_delete=models.CASCADE)
    ordre = models.ForeignKey(ORDRE,on_delete=models.CASCADE)
    famille = models.ForeignKey(FAMILLE,on_delete=models.CASCADE))
