from django.db import models
from GoMuscu.Muscle.models import MuscleModel


# Create your models here.

class ExerciceModel(models.Model) :
    name = models.CharField('Name', max_length=20, unique=True )
    desc = models.CharField('Description', max_length=500, unique=True)
    idMuscle = models.ForeignKey(MuscleModel, on_delete=models.CASCADE)

    def __str__(self): #self = this
        return self.name