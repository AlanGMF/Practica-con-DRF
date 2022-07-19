

from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import generics, mixins
from .serializers import UsuarioSerializer,NotaSerializer,ComentarioSerializer
from .models import Usuario,Nota,Comentario
 
def Profile(request):
    #put delete create update read user data
    #muestra las notas del usuario target
    pass

""" CRUD NOTA"""

class Nota_mixin_urd(
    generics.CreateAPIView,
    mixins.DestroyModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin
    ):
    queryset = Nota.objects.all()
    serializer_class= NotaSerializer
    lookup_field='pk' #necesita la espesificacion del campo a destruir
    
    def get(self, request, *args, **kwargs):
        return self.retrieve(request,*args, **kwargs)

class Crear_nota(generics.CreateAPIView):
    queryset = Nota.objects.all()
    serializer_class= NotaSerializer

""" CRUD COMENTARIO"""
class Comentario_mixin_urd(
    generics.GenericAPIView,
    mixins.DestroyModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin
    ):
    queryset = Comentario.objects.all()
    serializer_class= ComentarioSerializer
    lookup_field='pk'

    def get(self, request, *args, **kwargs):
        return self.retrieve(request,*args, **kwargs)
    

class Crear_comentario(generics.CreateAPIView):
    queryset = Comentario.objects.all()
    serializer_class= ComentarioSerializer


