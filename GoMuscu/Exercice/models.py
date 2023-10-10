from django.db import models


# Create your models here.

class ExerciceModel(models.Model) :
    name = models.CharField('Name', max_length=20, unique=True )
    desc = models.CharField('Description', max_length=500, unique=True)
    muscleName = models.CharField('Muscle Name', max_length=20, unique=False )

    def __str__(self): #self = this
        return self.name