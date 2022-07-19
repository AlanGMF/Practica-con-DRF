
from rest_framework import serializers
from .models import Nota,Comentario,Usuario



class NotaSerializer(serializers.ModelSerializer):
    class Meta:
        model= Nota
        fields=[
            "contenido",
            "created_at",
            "usuario",
            "coment",
        ]

        
class ComentarioSerializer(serializers.ModelSerializer):
    class Meta:
        model= Comentario
        fields=[
            "contenido",
            "created_at",
            "usuario",
            "nota",
        ]

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model= Usuario
        fields=[
            "mail",
            "nick_name",
            "birth_date",
            "sign_up",
            "user_name",
            "description" ,
        ]