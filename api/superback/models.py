
from django.db import models
from django.utils import timezone
# Create your models here.

#PONER ESTADO DE LA NOTA ACTIVO O DESACTIVO
#ALERTA NOTA
#GRUPO DE NOTAS, TIPO AGENDA
#que cuente cantidad de palabras y las enliste y enumere


class Usuario(models.Model):
    mail= models.EmailField(default="")
    nick_name= models.CharField(max_length=15)
    birth_date= models.DateField(default=timezone.now)
    sign_up= models.DateTimeField(default=timezone.now)
    user_name=models.CharField(max_length=15)
    description= models.CharField(max_length=50)
    


class Nota(models.Model):
    contenido=models.CharField(max_length=3000, default="")
    created_at= models.DateTimeField(default=timezone.now)
    usuario=models.ForeignKey(Usuario,on_delete=models.CASCADE)

    

class Comentario(models.Model):
    contenido=models.CharField(max_length=200,default="")
    created_at=models.DateTimeField(default=timezone.now)
    usuario=models.ForeignKey(Usuario,on_delete=models.CASCADE)
    nota=models.ForeignKey(Nota,on_delete=models.CASCADE,null=True,related_name='comentarios')

    def __str__(self):
        contenido=self.contenido

