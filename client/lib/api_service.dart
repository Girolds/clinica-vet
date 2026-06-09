import 'dart:convert';
import 'package:flutter/foundation.dart';
import 'package:http/http.dart' as http;
import 'package:shared_preferences/shared_preferences.dart';

class ApiService {
  // Configuração do IP:
  // 'http://127.0.0.1:8000' (Web / Emulador iOS).
  // 'http://10.0.2.2:8000' (Emulador Android)
  static const String baseUrl = 'http://127.0.0.1:8000';

  static const String clientId = '227aw7APqYR4wAvmmWA1XCi8NTxdRGdJPfxrqUME';
  static const String clientSecret =
      'DNNrkyIH3do7dq7idltdI5PaHwAwLgkqj2Vohn0uaL8XgTj5WM5sfEfJRxRY0sN5NtS88jBZBj4Mxb2xPgjs36MtNCZMa9MAliMPzgTqwqpHVKuXbRFGlyDPVu0Fcem7';

  // ==========================================
  // LOGIN E OBTENÇÃO DO TOKEN
  // ==========================================
  Future<bool> login(String username, String password) async {
    final url = Uri.parse('$baseUrl/o/token/');

    try {
      final response = await http.post(
        url,
        body: {
          'grant_type': 'password',
          'username': username,
          'password': password,
          'client_id': clientId,
          'client_secret': clientSecret,
        },
      );

      if (response.statusCode == 200) {
        final data = json.decode(response.body);
        final prefs = await SharedPreferences.getInstance();

        await prefs.setString('access_token', data['access_token']);
        return true;
      } else {
        debugPrint('Falha na autenticação: ${response.body}');
        return false;
      }
    } catch (e) {
      debugPrint('Erro de rede ao tentar fazer login: $e');
      return false;
    }
  }

  // ==========================================
  // LISTAR ANIMAIS (GET)
  // ==========================================
  Future<List<dynamic>> fetchAnimais() async {
    final url = Uri.parse('$baseUrl/api/animais/');
    final prefs = await SharedPreferences.getInstance();
    final token = prefs.getString('access_token');

    if (token == null) return [];

    try {
      final response = await http.get(
        url,
        headers: {
          'Authorization': 'Bearer $token',
          'Content-Type': 'application/json',
        },
      );

      if (response.statusCode == 200) {
        final data = json.decode(response.body);
        return data['results'] as List<dynamic>;
      } else {
        debugPrint('Erro ao obter dados: ${response.body}');
        return [];
      }
    } catch (e) {
      debugPrint('Erro de rede ao procurar animais: $e');
      return [];
    }
  }

  // ==========================================
  // CRIAR ANIMAL (POST)
  // ==========================================
  Future<bool> createAnimal(
    String nome,
    String especie,
    String raca,
    String tutorId,
  ) async {
    final url = Uri.parse('$baseUrl/api/animais/');
    final prefs = await SharedPreferences.getInstance();
    final token = prefs.getString('access_token');

    if (token == null) return false;

    try {
      final response = await http.post(
        url,
        headers: {
          'Authorization': 'Bearer $token',
          'Content-Type': 'application/json',
        },
        body: json.encode({
          'nome': nome,
          'especie': especie,
          'raca': raca,
          'tutor': int.tryParse(tutorId) ?? 1,
        }),
      );

      if (response.statusCode == 201) {
        return true;
      } else {
        debugPrint('Erro ao criar animal: ${response.body}');
        return false;
      }
    } catch (e) {
      debugPrint('Erro de rede ao criar animal: $e');
      return false;
    }
  }

  // ==========================================
  // ATUALIZAR ANIMAL (PUT)
  // ==========================================
  Future<bool> updateAnimal(
    int id,
    String nome,
    String especie,
    String raca,
    String tutorId,
  ) async {
    final url = Uri.parse('$baseUrl/api/animais/$id/');
    final prefs = await SharedPreferences.getInstance();
    final token = prefs.getString('access_token');

    if (token == null) return false;

    try {
      final response = await http.put(
        url,
        headers: {
          'Authorization': 'Bearer $token',
          'Content-Type': 'application/json',
        },
        body: json.encode({
          'nome': nome,
          'especie': especie,
          'raca': raca,
          'tutor': int.tryParse(tutorId) ?? 1,
        }),
      );

      return response.statusCode == 200;
    } catch (e) {
      debugPrint('Erro ao atualizar: $e');
      return false;
    }
  }

  // ==========================================
  // APAGAR ANIMAL (DELETE)
  // ==========================================
  Future<bool> deleteAnimal(int id) async {
    final url = Uri.parse('$baseUrl/api/animais/$id/');
    final prefs = await SharedPreferences.getInstance();
    final token = prefs.getString('access_token');

    if (token == null) return false;

    try {
      final response = await http.delete(
        url,
        headers: {'Authorization': 'Bearer $token'},
      );

      return response.statusCode == 204;
    } catch (e) {
      debugPrint('Erro ao apagar: $e');
      return false;
    }
  }
}
