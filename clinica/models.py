from django.db import models
from django.contrib.auth.models import User

# Tutores (Clientes)
class Tutor(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    
    nome = models.CharField(max_length=100)
    telefone = models.CharField(max_length=20)
    cpf = models.CharField(max_length=14, unique=True, help_text="Formato: 000.000.000-00")

    def __str__(self):
        return self.nome

# Veterinários
class Veterinario(models.Model):
    nome = models.CharField(max_length=100)
    crmv = models.CharField(max_length=20, unique=True, verbose_name="CRMV")
    especialidade = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.nome} ({self.especialidade})"

# Animais (Pacientes)
class Animal(models.Model):
    nome = models.CharField(max_length=50)
    especie = models.CharField(max_length=50, help_text="Ex: Cachorro, Gato")
    raca = models.CharField(max_length=50, verbose_name="Raça")
    # Pra deletar os animais caso delete o tutor (o dito cujo do cascade)
    tutor = models.ForeignKey(Tutor, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.nome} ({self.tutor.nome})"
    
    class Meta:
        verbose_name_plural = "Animais"

# Serviços
class Servico(models.Model):
    descricao = models.CharField(max_length=100, verbose_name="Descrição")
    valor = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.descricao} (R$ {self.valor})"
    
    class Meta:
        verbose_name = "Serviço"

# Agendamentos (oq conecta tudo)
class Agendamento(models.Model):
    animal = models.ForeignKey(Animal, on_delete=models.CASCADE)
    # Caso o veterinário saia da clínica, o histórico fica
    veterinario = models.ForeignKey(Veterinario, on_delete=models.SET_NULL, null=True)
    servico = models.ForeignKey(Servico, on_delete=models.SET_NULL, null=True, verbose_name="Serviço")
    data = models.DateTimeField(help_text="Formato: dia/mês/ano hora:minuto")
    observacao = models.TextField(blank=True, null=True, verbose_name="Observações")

    def __str__(self):
        return f"{self.animal.nome} - {self.data.strftime('%d/%m/%Y %H:%M')}"