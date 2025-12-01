from django import forms
from .models import Tutor, Animal

class TutorForm(forms.ModelForm):
    class Meta:
        model = Tutor
        fields = ['nome', 'telefone', 'cpf']

class AnimalForm(forms.ModelForm):
    class Meta:
        model = Animal
        fields = ['nome', 'especie', 'raca', 'tutor']
