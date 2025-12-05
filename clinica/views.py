from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, update_session_auth_hash
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import Animal, Tutor, Veterinario, Servico, Agendamento
from .forms import (
    AnimalForm, TutorForm, VeterinarioForm, ServicoForm, AgendamentoForm,
    UsuarioRegisterForm, PerfilForm, CustomPasswordChangeForm
)

def checar_admin(user):
    return user.is_staff

# -------------------------------------------------------
# PÁGINA INICIAL
# -------------------------------------------------------
def index(request):
    return render(request, 'clinica/index.html')

# -------------------------------------------------------
# GESTÃO DE USUÁRIOS
# -------------------------------------------------------
def registrar_usuario(request):
    if request.method == 'POST':
        form = UsuarioRegisterForm(request.POST)
        if form.is_valid():
            # 1. Salva o usuário no banco, mas não commita ainda para podermos editar
            user = form.save(commit=False)
            
            # 2. Verifica se o checkbox "is_admin" foi marcado
            if form.cleaned_data.get('is_admin'):
                user.is_staff = True
            
            # 3. Salva o usuário definitivamente
            user.save()

            # 4. Loga o usuário
            login(request, user)
            return redirect('index')
    else:
        form = UsuarioRegisterForm()
    
    return render(request, 'registration/register.html', {'form': form})

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

# -------------------------------------------------------
# TUTORES
# -------------------------------------------------------
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
    contexto = {'tutor': tutor, 'animais': animais, 'titulo': f'Ficha: {tutor.nome}'}
    return render(request, 'clinica/tutor_detalhe.html', contexto)

@login_required
@user_passes_test(checar_admin)
def tutor_editar(request, pk):
    tutor = get_object_or_404(Tutor, pk=pk)
    if request.method == 'POST':
        form = TutorForm(request.POST, instance=tutor)
        if form.is_valid():
            form.save()
            return redirect('tutor_lista')
    else:
        form = TutorForm(instance=tutor)
    contexto = {'form': form, 'titulo': f'Editar {tutor.nome}', 'botao': 'Salvar Alterações'}
    return render(request, 'clinica/form_generico.html', contexto)

@login_required
@user_passes_test(checar_admin)
def tutor_deletar(request, pk):
    tutor = get_object_or_404(Tutor, pk=pk)
    if request.method == 'POST':
        tutor.delete()
        return redirect('tutor_lista')
    contexto = {'objeto': tutor, 'titulo': 'Excluir Tutor'}
    return render(request, 'clinica/tutor_confirmar_delete.html', contexto)

# -------------------------------------------------------
# ANIMAIS
# -------------------------------------------------------
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

@login_required
@user_passes_test(checar_admin)
def animal_editar(request, pk):
    animal = get_object_or_404(Animal, pk=pk)
    if request.method == 'POST':
        form = AnimalForm(request.POST, instance=animal)
        if form.is_valid():
            form.save()
            return redirect('animal_lista')
    else:
        form = AnimalForm(instance=animal)
    contexto = {'form': form, 'titulo': f'Editar {animal.nome}', 'botao': 'Salvar Alterações'}
    return render(request, 'clinica/form_generico.html', contexto)

@login_required
@user_passes_test(checar_admin)
def animal_deletar(request, pk):
    animal = get_object_or_404(Animal, pk=pk)
    if request.method == 'POST':
        animal.delete()
        return redirect('animal_lista')
    contexto = {'animal': animal, 'titulo': 'Excluir Animal'}
    return render(request, 'clinica/animal_confirmar_delete.html', contexto)

# -------------------------------------------------------
# VETERINÁRIOS
# -------------------------------------------------------
@login_required
def veterinario_lista(request):
    veterinarios = Veterinario.objects.all()
    contexto = {'veterinarios': veterinarios, 'titulo': 'Corpo Clínico'}
    return render(request, 'clinica/veterinario_lista.html', contexto)

@login_required
def veterinario_detalhe(request, pk):
    veterinario = get_object_or_404(Veterinario, pk=pk)
    contexto = {'veterinario': veterinario, 'titulo': f'Dr(a). {veterinario.nome}'}
    return render(request, 'clinica/veterinario_detalhe.html', contexto)

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

@login_required
@user_passes_test(checar_admin)
def veterinario_editar(request, pk):
    veterinario = get_object_or_404(Veterinario, pk=pk)
    if request.method == 'POST':
        form = VeterinarioForm(request.POST, instance=veterinario)
        if form.is_valid():
            form.save()
            return redirect('veterinario_lista')
    else:
        form = VeterinarioForm(instance=veterinario)
    contexto = {'form': form, 'titulo': f'Editar {veterinario.nome}', 'botao': 'Atualizar'}
    return render(request, 'clinica/form_generico.html', contexto)

@login_required
@user_passes_test(checar_admin)
def veterinario_deletar(request, pk):
    veterinario = get_object_or_404(Veterinario, pk=pk)
    if request.method == 'POST':
        veterinario.delete()
        return redirect('veterinario_lista')
    contexto = {'objeto': veterinario, 'titulo': 'Remover Veterinário'}
    return render(request, 'clinica/veterinario_confirmar_delete.html', contexto)

# -------------------------------------------------------
# SERVIÇOS
# -------------------------------------------------------
@login_required
def servico_lista(request):
    servicos = Servico.objects.all()
    contexto = {'servicos': servicos, 'titulo': 'Tabela de Serviços'}
    return render(request, 'clinica/servico_lista.html', contexto)

@login_required
def servico_detalhe(request, pk):
    servico = get_object_or_404(Servico, pk=pk)
    contexto = {'servico': servico, 'titulo': servico.descricao}
    return render(request, 'clinica/servico_detalhe.html', contexto)

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

@login_required
@user_passes_test(checar_admin)
def servico_editar(request, pk):
    servico = get_object_or_404(Servico, pk=pk)
    if request.method == 'POST':
        form = ServicoForm(request.POST, instance=servico)
        if form.is_valid():
            form.save()
            return redirect('servico_lista')
    else:
        form = ServicoForm(instance=servico)
    contexto = {'form': form, 'titulo': f'Editar {servico.descricao}', 'botao': 'Atualizar Preço'}
    return render(request, 'clinica/form_generico.html', contexto)

@login_required
@user_passes_test(checar_admin)
def servico_deletar(request, pk):
    servico = get_object_or_404(Servico, pk=pk)
    if request.method == 'POST':
        servico.delete()
        return redirect('servico_lista')
    contexto = {'objeto': servico, 'titulo': 'Remover Serviço'}
    return render(request, 'clinica/servico_confirmar_delete.html', contexto)

# -------------------------------------------------------
# AGENDAMENTOS
# -------------------------------------------------------
@login_required
def agendamento_lista(request):
    agendamentos = Agendamento.objects.all().order_by('data')
    contexto = {'agendamentos': agendamentos, 'titulo': 'Agenda da Clínica'}
    return render(request, 'clinica/agendamento_lista.html', contexto)

@login_required
def agendamento_detalhe(request, pk):
    agendamento = get_object_or_404(Agendamento, pk=pk)
    contexto = {'agendamento': agendamento, 'titulo': f'Consulta: {agendamento.animal.nome}'}
    return render(request, 'clinica/agendamento_detalhe.html', contexto)

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
@user_passes_test(checar_admin)
def agendamento_editar(request, pk):
    agendamento = get_object_or_404(Agendamento, pk=pk)
    if request.method == 'POST':
        form = AgendamentoForm(request.POST, instance=agendamento)
        if form.is_valid():
            form.save()
            return redirect('agendamento_lista')
    else:
        form = AgendamentoForm(instance=agendamento)
    contexto = {'form': form, 'titulo': f'Reagendar: {agendamento.animal.nome}', 'botao': 'Salvar Nova Data'}
    return render(request, 'clinica/form_generico.html', contexto)

@login_required
@user_passes_test(checar_admin)
def agendamento_deletar(request, pk):
    agendamento = get_object_or_404(Agendamento, pk=pk)
    if request.method == 'POST':
        agendamento.delete()
        return redirect('agendamento_lista')
    contexto = {'objeto': agendamento, 'titulo': 'Cancelar Agendamento'}
    return render(request, 'clinica/agendamento_confirmar_delete.html', contexto)