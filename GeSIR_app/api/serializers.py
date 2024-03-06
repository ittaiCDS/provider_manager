from rest_framework import serializers
from .models import Proveedor, Cordenadas
from django.contrib.auth.models import User

class ProveedorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Proveedor
        fields = '__all__'
        
class CoordenadasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cordenadas
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'