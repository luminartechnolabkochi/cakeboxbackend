from django.contrib.auth.models import User
from rest_framework import serializers
from api.models import Cake,Cart,Order


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

class CartSerializer(serializers.ModelSerializer):
    user=serializers.CharField(read_only=True)
    status=serializers.CharField(read_only=True)
    cake=serializers.CharField(read_only=True)
    class Meta:
        model=Cart
        fields=["user","status","quantity","created_date","cake"]


class OrderSerializer(serializers.ModelSerializer):
    cake=serializers.CharField(read_only=True)
    user=serializers.CharField(read_only=True)
    created_date=serializers.CharField(read_only=True)
    status=serializers.CharField(read_only=True)
    expected_deliverydate=serializers.CharField(read_only=True)
    class Meta:
        model=Order
        fields=["cake","user","created_date","status","expected_deliverydate","address","matter"]