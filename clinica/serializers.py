# clinica/serializers.py
from rest_framework import serializers
from .models import Tutor, Animal, Veterinario, Servico, Agendamento

class TutorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tutor
        fields = '__all__'

class AnimalSerializer(serializers.ModelSerializer):
    # Opcional: podemos incluir o nome do tutor na resposta para facilitar no mobile
    tutor_nome = serializers.ReadOnlyField(source='tutor.nome')

    class Meta:
        model = Animal
        fields = ['id', 'nome', 'especie', 'raca', 'tutor', 'tutor_nome']

class AgendamentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Agendamento
        fields = '__all__'