from django.contrib import admin
from .models import Tutor, Veterinario, Animal, Servico, Agendamento


@admin.register(Tutor)
class TutorAdmin(admin.ModelAdmin):
    list_display = ('nome', 'telefone', 'cpf', 'usuario')
    search_fields = ('nome', 'cpf')

@admin.register(Veterinario)
class VeterinarioAdmin(admin.ModelAdmin):
    list_display = ('nome', 'crmv', 'especialidade')

@admin.register(Animal)
class AnimalAdmin(admin.ModelAdmin):
    list_display = ('nome', 'especie', 'raca', 'tutor')
    list_filter = ('especie',) 
@admin.register(Servico)
class ServicoAdmin(admin.ModelAdmin):
    list_display = ('descricao', 'valor')

@admin.register(Agendamento)
class AgendamentoAdmin(admin.ModelAdmin):
    list_display = ('data', 'animal', 'veterinario', 'servico')
    list_filter = ('data', 'veterinario')