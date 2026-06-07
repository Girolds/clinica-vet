from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .serializers import TutorSerializer, AnimalSerializer, AgendamentoSerializer

# API REST (ViewSets)

class TutorViewSet(viewsets.ModelViewSet):
    queryset = Tutor.objects.all()
    serializer_class = TutorSerializer
    permission_classes = [IsAuthenticated] # Rota protegida

class AnimalViewSet(viewsets.ModelViewSet):
    queryset = Animal.objects.all()
    serializer_class = AnimalSerializer
    permission_classes = [IsAuthenticated] # Rota protegida

class AgendamentoViewSet(viewsets.ModelViewSet):
    queryset = Agendamento.objects.all()
    serializer_class = AgendamentoSerializer
    permission_classes = [IsAuthenticated] # Rota protegida