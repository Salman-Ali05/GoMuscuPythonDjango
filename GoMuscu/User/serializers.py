from .models import UserModel
from rest_framework import serializers

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta :
        model = UserModel
        fields = ['userName', 'password']