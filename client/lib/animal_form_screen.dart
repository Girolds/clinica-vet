import 'package:flutter/material.dart';
import 'api_service.dart';

class AnimalFormScreen extends StatefulWidget {
  final Map<String, dynamic>?
  animal; // Se for nulo cria, se vier com dados edita.

  const AnimalFormScreen({super.key, this.animal});

  @override
  State<AnimalFormScreen> createState() => _AnimalFormScreenState();
}

class _AnimalFormScreenState extends State<AnimalFormScreen> {
  final _nomeController = TextEditingController();
  final _especieController = TextEditingController();
  final _racaController = TextEditingController();
  final _tutorController = TextEditingController();

  final _apiService = ApiService();
  bool _isLoading = false;

  @override
  void initState() {
    super.initState();
    // Se for edição, preenche os campos com os dados do bicho
    if (widget.animal != null) {
      _nomeController.text = widget.animal!['nome'] ?? '';
      _especieController.text = widget.animal!['especie'] ?? '';
      _racaController.text = widget.animal!['raca'] ?? '';
      _tutorController.text = widget.animal!['tutor']?.toString() ?? '';
    }
  }

  void _salvarAnimal() async {
    if (_nomeController.text.isEmpty || _tutorController.text.isEmpty) {
      ScaffoldMessenger.of(context).showSnackBar(
        const SnackBar(content: Text('Nome e ID do Tutor são obrigatórios!')),
      );
      return;
    }

    setState(() => _isLoading = true);

    bool success;
    if (widget.animal == null) {
      // MODO CRIAR (POST)
      success = await _apiService.createAnimal(
        _nomeController.text.trim(),
        _especieController.text.trim(),
        _racaController.text.trim(),
        _tutorController.text.trim(),
      );
    } else {
      // MODO EDITAR (PUT)
      success = await _apiService.updateAnimal(
        widget.animal!['id'],
        _nomeController.text.trim(),
        _especieController.text.trim(),
        _racaController.text.trim(),
        _tutorController.text.trim(),
      );
    }

    setState(() => _isLoading = false);

    if (success) {
      if (mounted) Navigator.pop(context, true);
    } else {
      if (mounted) {
        ScaffoldMessenger.of(context).showSnackBar(
          const SnackBar(content: Text('Erro ao salvar no servidor.')),
        );
      }
    }
  }

  @override
  Widget build(BuildContext context) {
    final isEditing = widget.animal != null;

    return Scaffold(
      backgroundColor: Colors.teal.shade50,
      appBar: AppBar(
        title: Text(isEditing ? 'Editar Paciente' : 'Novo Paciente'),
        backgroundColor: Colors.teal,
        foregroundColor: Colors.white,
      ),
      body: SingleChildScrollView(
        padding: const EdgeInsets.all(24.0),
        child: Container(
          padding: const EdgeInsets.all(24),
          decoration: BoxDecoration(
            color: Colors.white,
            borderRadius: BorderRadius.circular(24),
            boxShadow: [
              BoxShadow(
                color: Colors.teal.withOpacity(0.1),
                blurRadius: 20,
                offset: const Offset(0, 10),
              ),
            ],
          ),
          child: Column(
            children: [
              Icon(
                isEditing ? Icons.edit : Icons.add_circle_outline,
                size: 64,
                color: Colors.teal,
              ),
              const SizedBox(height: 24),
              TextField(
                controller: _nomeController,
                decoration: const InputDecoration(
                  labelText: 'Nome do Animal',
                  prefixIcon: Icon(Icons.pets),
                ),
              ),
              const SizedBox(height: 16),
              TextField(
                controller: _especieController,
                decoration: const InputDecoration(
                  labelText: 'Espécie (Ex: Cachorro)',
                ),
              ),
              const SizedBox(height: 16),
              TextField(
                controller: _racaController,
                decoration: const InputDecoration(
                  labelText: 'Raça (Ex: Poodle)',
                ),
              ),
              const SizedBox(height: 16),
              TextField(
                controller: _tutorController,
                keyboardType: TextInputType.number,
                decoration: const InputDecoration(
                  labelText: 'ID do Tutor (Número)',
                  prefixIcon: Icon(Icons.person),
                ),
              ),
              const SizedBox(height: 32),
              _isLoading
                  ? const CircularProgressIndicator()
                  : ElevatedButton(
                      onPressed: _salvarAnimal,
                      child: Text(
                        isEditing ? 'ATUALIZAR DADOS' : 'SALVAR PACIENTE',
                      ),
                    ),
            ],
          ),
        ),
      ),
    );
  }
}
