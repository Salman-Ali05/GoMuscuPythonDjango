from django.db import models


# Create your models here.

class MuscleModel(models.Model) :
    muscleName = models.CharField('Muscle Name', max_length=20, unique=True )

    def __str__(self): #self = this
        return self.muscleName
