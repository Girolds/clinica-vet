import 'dart:convert';
import 'package:flutter/foundation.dart'; 
import 'package:http/http.dart' as http;
import 'package:shared_preferences/shared_preferences.dart';


class ApiService {
  // Configuração do IP:
  // 'http://127.0.0.1:8000' (Web).
  // 'http://10.0.2.2:8000' (Emulador Android)
  static const String baseUrl = 'http://127.0.0.1:8000';

  static const String clientId = 'n1h2ev2nz8ZIzYa6kd1MAafQYdJJzzKQPTSmxMyh';
  static const String clientSecret = 'S9AYnr2wISP8gMoXs12HnXkHp944KAr4HoXKWuo17T661wasSeeTv1PQFu67Aa1tMkLJvParYEEGjk0gfltSfU9SCoGjDz28hExIx3eCqmzBTc6rpogLrkWSsVoqJsCb';


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
}