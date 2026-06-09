import 'package:flutter/material.dart';
import 'api_service.dart';
import 'login_screen.dart';
import 'animal_form_screen.dart';

class AnimalListScreen extends StatefulWidget {
  const AnimalListScreen({super.key});

  @override
  State<AnimalListScreen> createState() => _AnimalListScreenState();
}

class _AnimalListScreenState extends State<AnimalListScreen> {
  final _apiService = ApiService();
  List<dynamic> _animais = [];
  bool _isLoading = true;

  @override
  void initState() {
    super.initState();
    _loadAnimais();
  }

  void _loadAnimais() async {
    final dados = await _apiService.fetchAnimais();
    setState(() {
      _animais = dados;
      _isLoading = false;
    });
  }

  //FUNÇÃO: Apagar animal com confirmação
  void _apagarAnimal(int id) async {
    bool confirmar =
        await showDialog(
          context: context,
          builder: (context) => AlertDialog(
            title: const Text('Apagar Paciente'),
            content: const Text('Tem certeza que deseja apagar este registo?'),
            actions: [
              TextButton(
                onPressed: () => Navigator.pop(context, false),
                child: const Text('Cancelar'),
              ),
              TextButton(
                onPressed: () => Navigator.pop(context, true),
                child: const Text(
                  'Apagar',
                  style: TextStyle(color: Colors.red),
                ),
              ),
            ],
          ),
        ) ??
        false;

    if (confirmar) {
      setState(() => _isLoading = true);
      bool sucesso = await _apiService.deleteAnimal(id);
      if (sucesso) {
        _loadAnimais(); // Atualiza a lista
      } else {
        setState(() => _isLoading = false);
        if (mounted) {
          ScaffoldMessenger.of(
            context,
          ).showSnackBar(const SnackBar(content: Text('Erro ao apagar.')));
        }
      }
    }
  }

  //FUNÇÃO: Abrir o formulário para criar ou editar
  void _abrirFormulario({Map<String, dynamic>? animal}) async {
    final resultado = await Navigator.push(
      context,
      MaterialPageRoute(builder: (context) => AnimalFormScreen(animal: animal)),
    );

    // Se salvou com sucesso no formulário, recarrega a lista
    if (resultado == true) {
      setState(() => _isLoading = true);
      _loadAnimais();
    }
  }

  void _logout() {
    Navigator.of(
      context,
    ).pushReplacement(MaterialPageRoute(builder: (_) => const LoginScreen()));
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: Colors.grey.shade100,
      appBar: AppBar(
        title: const Text('Pacientes da Clínica'),
        backgroundColor: Colors.teal,
        foregroundColor: Colors.white,
        centerTitle: true,
        elevation: 0,
        actions: [
          IconButton(
            icon: const Icon(Icons.logout),
            tooltip: 'Sair',
            onPressed: _logout,
          ),
        ],
      ),
      body: _isLoading
          ? const Center(child: CircularProgressIndicator(color: Colors.teal))
          : _animais.isEmpty
          ? Center(
              child: Column(
                mainAxisAlignment: MainAxisAlignment.center,
                children: [
                  Icon(Icons.pets, size: 64, color: Colors.grey.shade400),
                  const SizedBox(height: 16),
                  const Text(
                    'Nenhum paciente registado ainda.',
                    style: TextStyle(fontSize: 16, color: Colors.grey),
                  ),
                ],
              ),
            )
          : ListView.builder(
              padding: const EdgeInsets.all(12),
              itemCount: _animais.length,
              itemBuilder: (context, index) {
                final animal = _animais[index];

                return Card(
                  elevation: 2,
                  margin: const EdgeInsets.symmetric(vertical: 8),
                  shape: RoundedRectangleBorder(
                    borderRadius: BorderRadius.circular(16),
                  ),
                  child: ListTile(
                    contentPadding: const EdgeInsets.symmetric(
                      horizontal: 16,
                      vertical: 8,
                    ),

                    // Avatar
                    leading: CircleAvatar(
                      radius: 28,
                      backgroundColor: Colors.teal.shade50,
                      child: const Icon(
                        Icons.pets,
                        color: Colors.teal,
                        size: 28,
                      ),
                    ),

                    // Nome do pet
                    title: Text(
                      animal['nome'] ?? 'Sem nome',
                      style: const TextStyle(
                        fontWeight: FontWeight.bold,
                        fontSize: 18,
                        color: Colors.black87,
                      ),
                    ),

                    // Espécie, Raça e Etiqueta do Tutor juntas
                    subtitle: Padding(
                      padding: const EdgeInsets.only(top: 4.0),
                      child: Column(
                        crossAxisAlignment: CrossAxisAlignment.start,
                        children: [
                          Text(
                            '${animal['especie']} • ${animal['raca']}',
                            style: TextStyle(color: Colors.grey.shade700),
                          ),
                          const SizedBox(height: 4),
                          Container(
                            padding: const EdgeInsets.symmetric(
                              horizontal: 8,
                              vertical: 4,
                            ),
                            decoration: BoxDecoration(
                              color: Colors.teal.shade100,
                              borderRadius: BorderRadius.circular(12),
                            ),
                            child: Text(
                              'Tutor ID: ${animal['tutor']}',
                              style: TextStyle(
                                color: Colors.teal.shade900,
                                fontWeight: FontWeight.w600,
                                fontSize: 11,
                              ),
                            ),
                          ),
                        ],
                      ),
                    ),

                    // Botões de Ação na direita
                    trailing: Row(
                      mainAxisSize: MainAxisSize.min,
                      children: [
                        IconButton(
                          icon: const Icon(Icons.edit, color: Colors.blue),
                          onPressed: () =>
                              _abrirFormulario(animal: animal), // Editar
                        ),
                        IconButton(
                          icon: const Icon(Icons.delete, color: Colors.red),
                          onPressed: () =>
                              _apagarAnimal(animal['id']), // Apagar
                        ),
                      ],
                    ),
                  ),
                );
              },
            ),

      // Botão flutuante para adicionar novos animais
      floatingActionButton: FloatingActionButton(
        onPressed: () => _abrirFormulario(),
        backgroundColor: Colors.teal,
        foregroundColor: Colors.white,
        child: const Icon(Icons.add),
      ),
    );
  }
}
