from rest_framework import serializers
from .models import Transaccion, Categoria
from django.contrib.auth.models import User

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = ['id', 'nombre'] # Muestra el id y el nombre de la categoría en el serializer este se implementa en el serializer de transacción

class TransaccionSerializer(serializers.ModelSerializer):
    categoria = CategoriaSerializer(read_only=True)
    categoria_id = serializers.PrimaryKeyRelatedField(
        queryset=Categoria.objects.all(), source='categoria', write_only=True
    ) # Muestra el id y el nombre de la categoría en el serializer

    class Meta:
        model = Transaccion
        fields = [
            'id',
            'usuario',
            'tipo',
            'descripcion',
            'monto',
            'fecha',
            'categoria',
            'categoria_id',
            'created_at',
        ]
        read_only_fields = ['id', 'created_at'] #Evita que el usuario pueda modificar el id y la fecha de creación

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def create(self, validated_data):
        user=User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )
        
        return user