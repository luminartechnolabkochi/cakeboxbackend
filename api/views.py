from django.shortcuts import render
from rest_framework.mixins import CreateModelMixin,ListModelMixin,RetrieveModelMixin
from rest_framework import serializers
from rest_framework.viewsets import GenericViewSet,ModelViewSet
from rest_framework import authentication,permissions
from django.contrib.auth.models import User
from api.serializers import UserSerializer,CakeSerializer
from api.models import Cake

# Create your views here

class UserView(GenericViewSet,CreateModelMixin):
    serializer_class=UserSerializer
    queryset=User.objects.all()

class CakeView(GenericViewSet,ListModelMixin,RetrieveModelMixin):
    serializer_class=CakeSerializer
    queryset=Cake.objects.all()
    authentication_classes=[authentication.TokenAuthentication]
    permission_classes=[permissions.IsAuthenticated]

    def get_queryset(self):
        qs=Cake.objects.all()

        if "layers" in self.request.query_params:
            lay=self.request.query_params.get("layers")
            qs=qs.filter(layers=lay)

        if "shape" in self.request.query_params:
            shp=self.request.query_params.get("shape")
            qs=qs.filter(shape=shp)
        return qs