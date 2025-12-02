from django.shortcuts import render, redirect, get_object_or_404
# Faltava este import abaixo para o @login_required funcionar:
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

from .models import Animal, Tutor, Veterinario, Servico, Agendamento
from .forms import AnimalForm, TutorForm, VeterinarioForm, ServicoForm, AgendamentoForm


# Página Inicial (Deixamos pública para aparecer a capa bonita)
def index(request):
    return render(request, 'clinica/index.html')

# =======================================================
# AUTENTICAÇÃO
# =======================================================
def registrar_usuario(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
    else:
        form = UserCreationForm()
    
    contexto = {'form': form, 'titulo': 'Criar Conta', 'botao': 'Cadastrar-se'}
    return render(request, 'registration/register.html', contexto)


# =======================================================
# ANIMAIS (Protegidos com @login_required)
# =======================================================
@login_required
def animal_lista(request):
    animais = Animal.objects.all()
    contexto = {'animais': animais, 'titulo': 'Todos os Animais'}
    return render(request, 'clinica/animal_lista.html', contexto)

@login_required
def animal_detalhe(request, pk):
    animal = get_object_or_404(Animal, pk=pk)
    contexto = {'animal': animal, 'titulo': f'Detalhes de {animal.nome}'}
    return render(request, 'clinica/animal_detalhe.html', contexto)

@login_required
def animal_criar(request):
    if request.method == 'POST':
        form = AnimalForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('animal_lista')
    else:
        form = AnimalForm()
    
    contexto = {'form': form, 'titulo': 'Cadastrar Novo Animal', 'botao': 'Cadastrar'}
    return render(request, 'clinica/form_generico.html', contexto)


# =======================================================
# TUTORES (Protegidos)
# =======================================================
@login_required
def tutor_lista(request):
    tutores = Tutor.objects.all()
    contexto = {'tutores': tutores, 'titulo': 'Gerenciar Tutores'}
    return render(request, 'clinica/tutor_lista.html', contexto)

@login_required
def tutor_criar(request):
    if request.method == 'POST':
        form = TutorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('tutor_lista')
    else:
        form = TutorForm()
    
    contexto = {'form': form, 'titulo': 'Cadastrar Novo Tutor', 'botao': 'Salvar Tutor'}
    return render(request, 'clinica/form_generico.html', contexto)

@login_required
def tutor_detalhe(request, pk):
    tutor = get_object_or_404(Tutor, pk=pk)
    animais = Animal.objects.filter(tutor=tutor)
    contexto = {
        'tutor': tutor,
        'animais': animais,
        'titulo': f'Ficha: {tutor.nome}'
    }
    return render(request, 'clinica/tutor_detalhe.html', contexto)


# =======================================================
# VETERINÁRIOS (Protegidos)
# =======================================================
@login_required
def veterinario_lista(request):
    veterinarios = Veterinario.objects.all()
    contexto = {'veterinarios': veterinarios, 'titulo': 'Corpo Clínico'}
    return render(request, 'clinica/veterinario_lista.html', contexto)

@login_required
def veterinario_criar(request):
    if request.method == 'POST':
        form = VeterinarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('veterinario_lista')
    else:
        form = VeterinarioForm()
    
    contexto = {'form': form, 'titulo': 'Cadastrar Veterinário', 'botao': 'Salvar'}
    return render(request, 'clinica/form_generico.html', contexto)


# =======================================================
# SERVIÇOS (Protegidos)
# =======================================================
@login_required
def servico_lista(request):
    servicos = Servico.objects.all()
    contexto = {'servicos': servicos, 'titulo': 'Tabela de Serviços'}
    return render(request, 'clinica/servico_lista.html', contexto)

@login_required
def servico_criar(request):
    if request.method == 'POST':
        form = ServicoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('servico_lista')
    else:
        form = ServicoForm()
    
    contexto = {'form': form, 'titulo': 'Novo Serviço', 'botao': 'Cadastrar'}
    return render(request, 'clinica/form_generico.html', contexto)


# =======================================================
# AGENDAMENTOS (Protegidos)
# =======================================================
@login_required
def agendamento_lista(request):
    agendamentos = Agendamento.objects.all().order_by('data')
    contexto = {'agendamentos': agendamentos, 'titulo': 'Agenda da Clínica'}
    return render(request, 'clinica/agendamento_lista.html', contexto)

@login_required
def agendamento_criar(request):
    if request.method == 'POST':
        form = AgendamentoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('agendamento_lista')
    else:
        form = AgendamentoForm()
    
    contexto = {'form': form, 'titulo': 'Agendar Consulta', 'botao': 'Agendar'}
    return render(request, 'clinica/form_generico.html', contexto)

@login_required
def agendamento_detalhe(request, pk):
    agendamento = get_object_or_404(Agendamento, pk=pk)
    contexto = {'agendamento': agendamento, 'titulo': f'Consulta: {agendamento.animal.nome}'}
    return render(request, 'clinica/agendamento_detalhe.html', contexto)