from .models import ExerciceModel
from rest_framework import serializers

class ExerciceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta :
        model = ExerciceModel
        # fields = '__all__' # get all fields, but better to specify which fields you're trying to get
        fields = ('id', 'name', 'desc', 'muscleName')