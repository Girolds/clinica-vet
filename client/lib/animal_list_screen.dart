import 'package:flutter/material.dart';
import 'api_service.dart';

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

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text('Animais Registados (API)')),
      body: _isLoading
          ? const Center(child: CircularProgressIndicator())
          : _animais.isEmpty
              ? const Center(child: Text('Nenhum animal encontrado ou erro de permissão.'))
              : ListView.builder(
                  itemCount: _animais.length,
                  itemBuilder: (context, index) {
                    final animal = _animais[index];
                    return ListTile(
                      leading: const Icon(Icons.pets),
                      title: Text(animal['nome'] ?? 'Sem nome'),
                      subtitle: Text('${animal['especie']} - ${animal['raca']}'),
                      trailing: Chip(
                        label: Text('Tutor ID: ${animal['tutor']}'),
                      ),
                    );
                  },
                ),
    );
  }
}