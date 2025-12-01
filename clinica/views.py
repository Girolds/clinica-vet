from django.shortcuts import render, redirect, get_object_or_404
from .models import Animal
from .forms import AnimalForm


def index(request):
    return render(request, 'clinica/index.html')


def animal_lista(request):
    animais = Animal.objects.all()
    contexto = {
        'animais': animais,
        'titulo': 'Todos os Animais'
    }
    return render(request, 'clinica/animal_lista.html', contexto)


def animal_detalhe(request, pk):
    animal = get_object_or_404(Animal, pk=pk)
    contexto = {
        'animal': animal,
        'titulo': f'Detalhes de {animal.nome}'
    }
    return render(request, 'clinica/animal_detalhe.html', contexto)


def animal_criar(request):
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