# 🏥 VetLife System

> **Sistema de Gestão para Clínicas Veterinárias**

Projeto desenvolvido como Trabalho Final da disciplina de **Programação para Web II** do curso de Tecnologia em Análise e Desenvolvimento de Sistemas. O projeto evoluiu de um sistema monolítico para um ecossistema com arquitetura distribuída, separando a inteligência de armazenamento (API RESTful) da interface de consumo (Cliente Multiplataforma em Flutter).

---

## 👥 Integrantes do Grupo
* **Geraldo Rafael Lopes Benevides**
* **Júlia Évelyn Magalhães dos Santos**

---

## 🎥 Vídeo de Apresentação

Confira o funcionamento do sistema, a arquitetura da API, o fluxo de segurança OAuth2 e a integração com o aplicativo nas rotas:

[![Assista ao vídeo de apresentação](https://youtu.be/C7F27Hs5DxM.jpg)](https://youtu.be/C7F27Hs5DxM)

> *Clique na imagem acima ou [neste link](https://youtu.be/C7F27Hs5DxM) para assistir.*

---

## 🚀 Funcionalidades Principais

### 🔒 Autenticação e Segurança (OAuth 2.0)
* **Tokens de Acesso:** Substituição de sessões tradicionais por comunicação *stateless* utilizando *Bearer Tokens*.
* **Integração Segura:** Fluxo de login via *Resource Owner Password Credentials Grant* configurado pelo Django OAuth Toolkit (DOT).
* **Proteção de Rotas:** Bloqueio de *endpoints* no DRF e redirecionamento automático de usuários não autenticados no aplicativo Flutter.

### 📋 Módulos de Gerenciamento (API CRUD)
* **Tutores & Animais:** Relacionamento estruturado e listagens com suporte a buscas indexadas (`SearchFilter` para nome, CPF, espécie e raça).
* **Equipe Médica & Serviços:** Cadastro de veterinários (com validação única de CRMV) e catálogo de procedimentos.
* **Agendamentos:** Marcação de consultas integrando *Animal + Veterinário + Serviço*.
* **Regras de Negócio:** Interceptação via `AgendamentoSerializer` para impedir agendamentos em datas retroativas.
* **Otimização:** Paginação global nativa para otimizar o tráfego de rede e o consumo de memória no cliente.

---

## 🛠 Tecnologias Utilizadas

| Camada | Tecnologia Principal | Ferramentas e Bibliotecas |
| :--- | :--- | :--- |
| **Backend (API)** | Python 3.12+ | Django 5, Django Rest Framework (DRF) |
| **Segurança** | OAuth 2.0 | Django OAuth Toolkit (DOT), django-cors-headers |
| **Banco de Dados**| SQLite3 | ORM Nativo do Django |
| **Frontend (App)**| Dart | Flutter (Web/Mobile) |
| **Versionamento** | Git | GitHub |

---

## 📦 Guia de Instalação e Execução

O projeto agora adota o padrão *monorepo*. Siga os passos abaixo utilizando **dois terminais independentes** (um para a API e outro para o App).

### Passo 1: Clonar o Repositório
Primeiro, baixe o código para sua máquina:
```bash
git clone [https://github.com/Girolds/clinica-vet.git](https://github.com/Girolds/clinica-vet.git)
cd clinica-vet