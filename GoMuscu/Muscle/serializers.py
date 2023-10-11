from .models import MuscleModel
from rest_framework import serializers

class MuscleSerializer(serializers.HyperlinkedModelSerializer):
    class Meta :
        model = MuscleModel
        fields = ['muscleName']