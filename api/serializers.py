from django.contrib.auth.models import User
from rest_framework import serializers
from api.models import Cake


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=["username","email","password"]

    def create(self, validated_data):
       return User.objects.create_user(**validated_data)
    

class CakeSerializer(serializers.ModelSerializer):
    id=serializers.IntegerField(read_only=True)
    class Meta:
        model=Cake
        fields="__all__"