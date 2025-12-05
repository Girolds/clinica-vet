from django import forms
from .models import Tutor, Animal, Veterinario, Servico, Agendamento
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm

# Formulário dos Tut.
class TutorForm(forms.ModelForm):
    class Meta:
        model = Tutor
        fields = ['nome', 'telefone', 'cpf']
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nome completo'}),
            'telefone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '(XX) 9XXXX-XXXX'}),
            'cpf': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '000.000.000-00'}),
        }

# Formulário dos Vet.
class VeterinarioForm(forms.ModelForm):
    class Meta:
        model = Veterinario
        fields = ['nome', 'crmv', 'especialidade']
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
            'crmv': forms.TextInput(attrs={'class': 'form-control'}),
            'especialidade': forms.TextInput(attrs={'class': 'form-control'}),
        }

# Formulário dos Animaizinhos
class AnimalForm(forms.ModelForm):
    class Meta:
        model = Animal
        fields = ['nome', 'especie', 'raca', 'tutor']
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
            'especie': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ex: Cachorro, Gato'}),
            'raca': forms.TextInput(attrs={'class': 'form-control'}),
            'tutor': forms.Select(attrs={'class': 'form-control'}), 
        }

# Formulário de Serviços
class ServicoForm(forms.ModelForm):
    class Meta:
        model = Servico
        fields = ['descricao', 'valor']
        widgets = {
            'descricao': forms.TextInput(attrs={'class': 'form-control'}),
            'valor': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
        }


class AgendamentoForm(forms.ModelForm):
    class Meta:
        model = Agendamento
        fields = ['animal', 'veterinario', 'servico', 'data', 'observacao']
        widgets = {
            'animal': forms.Select(attrs={'class': 'form-control'}),
            'veterinario': forms.Select(attrs={'class': 'form-control'}),
            'servico': forms.Select(attrs={'class': 'form-control'}),
            'data': forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'datetime-local'}),
            'observacao': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }

class UsuarioRegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control'})


class PerfilForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'username']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'username': forms.TextInput(attrs={'class': 'form-control'}),
        }


class CustomPasswordChangeForm(PasswordChangeForm):
    # Injetando CSS do Bootstrap nos campos de senha
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control'})