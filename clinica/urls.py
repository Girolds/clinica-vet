from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    
    # Rotas de Animais (Apenas o que já existe na View)
    path('animais/', views.animal_lista, name='animal_lista'),
    path('animais/novo/', views.animal_criar, name='animal_criar'),
    path('animais/<int:pk>/', views.animal_detalhe, name='animal_detalhe'),
]