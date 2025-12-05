from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from .models import Tutor, Animal, Veterinario, Servico, Agendamento

# =======================================================
# FORMULÁRIOS DE NEGÓCIO
# =======================================================

class TutorForm(forms.ModelForm):
    class Meta:
        model = Tutor
        fields = ['nome', 'telefone', 'cpf']
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nome completo'}),
            'telefone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '(XX) 9XXXX-XXXX'}),
            'cpf': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '000.000.000-00'}),
        }

class VeterinarioForm(forms.ModelForm):
    class Meta:
        model = Veterinario
        fields = ['nome', 'crmv', 'especialidade']
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
            'crmv': forms.TextInput(attrs={'class': 'form-control'}),
            'especialidade': forms.TextInput(attrs={'class': 'form-control'}),
        }

class AnimalForm(forms.ModelForm):
    class Meta:
        model = Animal
        fields = ['nome', 'especie', 'raca', 'tutor']
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
            'especie': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ex: Cachorro, Gato'}),
            'raca': forms.TextInput(attrs={'class': 'form-control'}),
            'tutor': forms.Select(attrs={'class': 'form-select'}), 
        }

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
            'animal': forms.Select(attrs={'class': 'form-select'}),
            'veterinario': forms.Select(attrs={'class': 'form-select'}),
            'servico': forms.Select(attrs={'class': 'form-select'}),
            'data': forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'datetime-local'}),
            'observacao': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }

# =======================================================
# FORMULÁRIOS DE USUÁRIO (Auth)
# =======================================================

class UsuarioRegisterForm(UserCreationForm):
    is_admin = forms.BooleanField(
        required=False, 
        label="É Administrador?",
        help_text="Marque se este usuário deve ter acesso administrativo.",
        widget=forms.CheckboxInput(attrs={'class': 'form-check-input'})
    )

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            if field != 'is_admin': 
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
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control'})