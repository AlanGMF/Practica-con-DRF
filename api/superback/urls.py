



from django.urls import path
from . import views
urlpatterns = [
    
  path('nota/<int:pk>/', views.Nota_mixin_urd.as_view() ),
  path('nota/', views.Crear_nota.as_view() ),
  path('comentario/<int:pk>/', views.Comentario_mixin_urd.as_view()),
  path('comentario/', views.Crear_comentario.as_view()),

]