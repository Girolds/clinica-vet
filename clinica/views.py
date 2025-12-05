from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.contrib.auth import login
from .forms import PerfilForm
from .forms import PerfilForm, CustomPasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from .models import Animal
from .forms import AnimalForm
from .models import Animal, Tutor
from .forms import AnimalForm, TutorForm
from .models import Animal, Tutor, Veterinario
from .forms import AnimalForm, TutorForm, VeterinarioForm
from .models import Animal, Tutor, Veterinario, Servico 
from .forms import AnimalForm, TutorForm, VeterinarioForm, ServicoForm
from .models import Animal, Tutor, Veterinario, Servico, Agendamento
from .forms import AnimalForm, TutorForm, VeterinarioForm, ServicoForm, AgendamentoForm, UsuarioRegisterForm


def is_recepcionista(user):
    return user.groups.filter(name='Recepcionistas').exists() or user.is_superuser


# =======================================================
# Parte do CRUD completo dos Animais
# =======================================================

# Read (Ler)

@login_required
def animal_lista(request):
    if is_recepcionista(request.user):
        animais = Animal.objects.all()
    else:
        animais = Animal.objects.filter(tutor__usuario=request.user)
    
    contexto = {'animais': animais, 'titulo': 'Meus Animais' if not is_recepcionista(request.user) else 'Todos os Animais'}
    return render(request, 'clinica/animal_lista.html', contexto)

# Detail (Detalhar)
@login_required
def animal_detalhe(request, pk):
    animal = get_object_or_404(Animal, pk=pk)
    
    contexto = {
        'animal': animal,
        'titulo': f'Detalhes de {animal.nome}'
    }
    return render(request, 'clinica/animal_detalhe.html', contexto)

# Create (Criar)
@login_required
def animal_criar(request):
  
    if not is_recepcionista(request.user):
        raise PermissionDenied("Apenas recepcionistas podem cadastrar.")
    
    if request.method == 'POST':
        form = AnimalForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('animal_lista')
    else:
        form = AnimalForm()
    
    contexto = {
        'form': form,
        'titulo': 'Cadastrar Novo Animal',
        'botao': 'Cadastrar'
    }
    return render(request, 'clinica/form_generico.html', contexto)

# Update (Editar/Atualizar)
@login_required
def animal_editar(request, pk):
    if not is_recepcionista(request.user):
        raise PermissionDenied("Apenas recepcionistas podem editar.") # Bloqueio de segurança
    
    animal = get_object_or_404(Animal, pk=pk)
    
    if request.method == 'POST':
        form = AnimalForm(request.POST, instance=animal)
        if form.is_valid():
            form.save()
            return redirect('animal_lista')
    else:
        form = AnimalForm(instance=animal)
    
    contexto = {
        'form': form,
        'titulo': f'Editar {animal.nome}',
        'botao': 'Salvar Alterações'
    }
    return render(request, 'clinica/form_generico.html', contexto)

# Delete (Deletar/Excluir)
@login_required
def animal_deletar(request, pk):
    if not is_recepcionista(request.user):
        raise PermissionDenied("Apenas recepcionistas podem excluir.") # Bloqueio de segurança
    
    animal = get_object_or_404(Animal, pk=pk)
    
    if request.method == 'POST':
        animal.delete()
        return redirect('animal_lista')
    
    contexto = {
        'animal': animal,
        'titulo': 'Excluir Animal'
    }
    return render(request, 'clinica/animal_confirmar_delete.html', contexto)

def index(request):
    return render(request, 'clinica/index.html')


# =======================================================
# Parte do CRUD completo dos Tutores
# =======================================================

# Read (Ler)
@login_required
def tutor_lista(request):
    tutores = Tutor.objects.all()
    contexto = {
        'tutores': tutores,
        'titulo': 'Gerenciar Tutores'
    }
    return render(request, 'clinica/tutor_lista.html', contexto)

# Detail (Detalhar)
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

# Create (Criar)
@login_required
def tutor_criar(request):
    if not is_recepcionista(request.user):
        raise PermissionDenied("Apenas recepcionistas podem cadastrar.") # Bloqueio de segurança
    
    if request.method == 'POST':
        form = TutorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('tutor_lista')
    else:
        form = TutorForm()
    
    contexto = {
        'form': form,
        'titulo': 'Cadastrar Novo Tutor',
        'botao': 'Salvar Tutor'
    }
    return render(request, 'clinica/form_generico.html', contexto)

# Update (Editar/Atualizar)
@login_required
def tutor_editar(request, pk):
    if not is_recepcionista(request.user):
        raise PermissionDenied("Apenas recepcionistas podem editar.") # Bloqueio de segurança
    
    tutor = get_object_or_404(Tutor, pk=pk)
    if request.method == 'POST':
        form = TutorForm(request.POST, instance=tutor)
        if form.is_valid():
            form.save()
            return redirect('tutor_lista')
    else:
        form = TutorForm(instance=tutor)
    
    contexto = {
        'form': form,
        'titulo': f'Editar {tutor.nome}',
        'botao': 'Salvar Alterações'
    }
    return render(request, 'clinica/form_generico.html', contexto)

# Delete (Deletar)
@login_required
def tutor_deletar(request, pk):
    if not is_recepcionista(request.user):
        raise PermissionDenied("Apenas recepcionistas podem excluir.") # Bloqueio de segurança
    
    tutor = get_object_or_404(Tutor, pk=pk)
    if request.method == 'POST':
        tutor.delete()
        return redirect('tutor_lista')
    
    contexto = {
        'objeto': tutor,
        'titulo': 'Excluir Tutor'
    }
    return render(request, 'clinica/tutor_confirmar_delete.html', contexto)


# =======================================================
# Parte do CRUD completo dos Veterinários
# =======================================================

# Read (Ler)
@login_required
def veterinario_lista(request):
    veterinarios = Veterinario.objects.all()
    contexto = {
        'veterinarios': veterinarios,
        'titulo': 'Corpo Clínico'
    }
    return render(request, 'clinica/veterinario_lista.html', contexto)

# Detail (Detalhar)
@login_required
def veterinario_detalhe(request, pk):
    veterinario = get_object_or_404(Veterinario, pk=pk)
    contexto = {
        'veterinario': veterinario,
        'titulo': f'Dr(a). {veterinario.nome}'
    }
    return render(request, 'clinica/veterinario_detalhe.html', contexto)

# Create (Criar)
@login_required
def veterinario_criar(request):
    if not is_recepcionista(request.user):
        raise PermissionDenied("Apenas recepcionistas podem cadastrar.") # Bloqueio de segurança
    
    if request.method == 'POST':
        form = VeterinarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('veterinario_lista')
    else:
        form = VeterinarioForm()
    
    contexto = {
        'form': form,
        'titulo': 'Cadastrar Veterinário',
        'botao': 'Salvar'
    }
    return render(request, 'clinica/form_generico.html', contexto) 

# Update (Editar/Atualizar)
@login_required
def veterinario_editar(request, pk):
    if not is_recepcionista(request.user):
        raise PermissionDenied("Apenas recepcionistas podem editar.") # Bloqueio de segurança
    
    veterinario = get_object_or_404(Veterinario, pk=pk)
    if request.method == 'POST':
        form = VeterinarioForm(request.POST, instance=veterinario)
        if form.is_valid():
            form.save()
            return redirect('veterinario_lista')
    else:
        form = VeterinarioForm(instance=veterinario)
    
    contexto = {
        'form': form,
        'titulo': f'Editar Dr(a). {veterinario.nome}',
        'botao': 'Atualizar'
    }
    return render(request, 'clinica/form_generico.html', contexto) 

# Delete (Deletar/Excluir)
@login_required
def veterinario_deletar(request, pk):
    if not is_recepcionista(request.user):
        raise PermissionDenied("Apenas recepcionistas podem excluir.") # Bloqueio de segurança
    
    veterinario = get_object_or_404(Veterinario, pk=pk)
    if request.method == 'POST':
        veterinario.delete()
        return redirect('veterinario_lista')
    
    contexto = {
        'objeto': veterinario,
        'titulo': 'Remover Veterinário'
    }
    return render(request, 'clinica/veterinario_confirmar_delete.html', contexto)

# =======================================================
# Parte do CRUD completo dos Serviços
# =======================================================

# Read (Ler)
@login_required
def servico_lista(request):
    servicos = Servico.objects.all()
    contexto = {
        'servicos': servicos,
        'titulo': 'Tabela de Serviços'
    }
    return render(request, 'clinica/servico_lista.html', contexto)

# Detail (Detalhar)
@login_required
def servico_detalhe(request, pk):
    servico = get_object_or_404(Servico, pk=pk)
    contexto = {
        'servico': servico,
        'titulo': servico.descricao
    }
    return render(request, 'clinica/servico_detalhe.html', contexto)

# Create (Criar)
@login_required
def servico_criar(request):
    if not is_recepcionista(request.user):
        raise PermissionDenied("Apenas recepcionistas podem cadastrar.") # Bloqueio de segurança
    
    if request.method == 'POST':
        form = ServicoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('servico_lista')
    else:
        form = ServicoForm()
    
    contexto = {
        'form': form,
        'titulo': 'Novo Serviço',
        'botao': 'Cadastrar'
    }
    return render(request, 'clinica/form_generico.html', contexto)

# Update (Editar/Atualizar)
@login_required
def servico_editar(request, pk):
    if not is_recepcionista(request.user):
        raise PermissionDenied("Apenas recepcionistas podem editar.") # Bloqueio de segurança
    
    servico = get_object_or_404(Servico, pk=pk)
    if request.method == 'POST':
        form = ServicoForm(request.POST, instance=servico)
        if form.is_valid():
            form.save()
            return redirect('servico_lista')
    else:
        form = ServicoForm(instance=servico)
    
    contexto = {
        'form': form,
        'titulo': f'Editar {servico.descricao}',
        'botao': 'Atualizar Preço'
    }
    return render(request, 'clinica/form_generico.html', contexto)

# Delete (Deletar/Excluir)
@login_required
def servico_deletar(request, pk):
    if not is_recepcionista(request.user):
        raise PermissionDenied("Apenas recepcionistas podem excluir.") # Bloqueio de segurança
    
    servico = get_object_or_404(Servico, pk=pk)
    if request.method == 'POST':
        servico.delete()
        return redirect('servico_lista')
    
    contexto = {
        'objeto': servico,
        'titulo': 'Remover Serviço'
    }
    return render(request, 'clinica/servico_confirmar_delete.html', contexto)


# =======================================================
# Parte do CRUD completo dos Agendamentos
# =======================================================

# Read (Ler)
@login_required
def agendamento_lista(request):
    if is_recepcionista(request.user):
        agendamentos = Agendamento.objects.all().order_by('data')
    else:
        
        agendamentos = Agendamento.objects.filter(animal__tutor__usuario=request.user).order_by('data')

    contexto = {'agendamentos': agendamentos, 'titulo': 'Minha Agenda' if not is_recepcionista(request.user) else 'Agenda da Clínica'}
    return render(request, 'clinica/agendamento_lista.html', contexto)

# Detail (Detalhar)
@login_required
def agendamento_detalhe(request, pk):
    agendamento = get_object_or_404(Agendamento, pk=pk)
    contexto = {
        'agendamento': agendamento,
        'titulo': f'Consulta: {agendamento.animal.nome}'
    }
    return render(request, 'clinica/agendamento_detalhe.html', contexto)

# Create (Criar)
@login_required
def agendamento_criar(request):
    if not is_recepcionista(request.user):
        raise PermissionDenied("Apenas recepcionistas podem cadastrar.") # Bloqueio de segurança
    
    if request.method == 'POST':
        form = AgendamentoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('agendamento_lista')
    else:
        form = AgendamentoForm()
    
    contexto = {
        'form': form,
        'titulo': 'Agendar Nova Consulta',
        'botao': 'Agendar'
    }
    return render(request, 'clinica/form_generico.html', contexto)

# Update (Editar/Atualizar)
@login_required
def agendamento_editar(request, pk):
    if not is_recepcionista(request.user):
        raise PermissionDenied("Apenas recepcionistas podem editar.") # Bloqueio de segurança
    
    agendamento = get_object_or_404(Agendamento, pk=pk)
    if request.method == 'POST':
        form = AgendamentoForm(request.POST, instance=agendamento)
        if form.is_valid():
            form.save()
            return redirect('agendamento_lista')
    else:
        form = AgendamentoForm(instance=agendamento)
    
    contexto = {
        'form': form,
        'titulo': f'Reagendar: {agendamento.animal.nome}',
        'botao': 'Salvar Nova Data'
    }
    return render(request, 'clinica/form_generico.html', contexto)

# Delete (Deletar/Excluir)
@login_required
def agendamento_deletar(request, pk):
    if not is_recepcionista(request.user):
        raise PermissionDenied("Apenas recepcionistas podem excluir.") # Bloqueio de segurança
    
    agendamento = get_object_or_404(Agendamento, pk=pk)
    if request.method == 'POST':
        agendamento.delete()
        return redirect('agendamento_lista')
    
    contexto = {
        'objeto': agendamento,
        'titulo': 'Cancelar Agendamento'
    }
    return render(request, 'clinica/agendamento_confirmar_delete.html', contexto)

def registrar_usuario(request):
    if request.method == 'POST':
        form = UsuarioRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            
            login(request, user)
            return redirect('index')
    else:
        form = UsuarioRegisterForm()
    
    return render(request, 'registration/register.html', {'form': form})


# Editar Dados Pessoais do usuário
@login_required
def editar_perfil(request):
    if request.method == 'POST':
        form = PerfilForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = PerfilForm(instance=request.user)
    
    return render(request, 'registration/perfil_editar.html', {'form': form})

# Alterar Senha usuário
@login_required
def alterar_senha(request):
    if request.method == 'POST':
       
        form = CustomPasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()

            update_session_auth_hash(request, user) 
            return redirect('index')
    else:
        form = CustomPasswordChangeForm(request.user)

    return render(request, 'registration/perfil_senha.html', {'form': form})