from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('animais/', views.animal_lista, name='animal_lista'),
    path('animais/novo/', views.animal_criar, name='animal_criar'),
    path('animais/<int:pk>/', views.animal_detalhe, name='animal_detalhe'),
    path('tutores/', views.tutor_lista, name='tutor_lista'),
    path('tutores/novo/', views.tutor_criar, name='tutor_criar'),
    path('tutores/<int:pk>/', views.tutor_detalhe, name='tutor_detalhe'),
    path('veterinarios/', views.veterinario_lista, name='veterinario_lista'),
    path('veterinarios/novo/', views.veterinario_criar, name='veterinario_criar'),
    path('servicos/', views.servico_lista, name='servico_lista'),
    path('servicos/novo/', views.servico_criar, name='servico_criar'),
    path('agendamentos/', views.agendamento_lista, name='agendamento_lista'),
    path('agendamentos/novo/', views.agendamento_criar, name='agendamento_criar'),
    path('agendamentos/<int:pk>/', views.agendamento_detalhe, name='agendamento_detalhe'),
]