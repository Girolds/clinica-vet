# 🏥 VetLife System

> **Sistema de Gestão para Clínicas Veterinárias**

Projeto desenvolvido como Trabalho Final da disciplina de **Programação para Web I**. O sistema oferece uma solução completa para o gerenciamento de pacientes, tutores, corpo clínico e agendamentos, com foco em usabilidade e segurança.

---

## 👥 Integrantes do Grupo
* **Geraldo Rafael Lopes Benevides**
* **Júlia Évelyn Magalhães dos Santos**

---

## 🎥 Vídeo de Apresentação

Confira o funcionamento do sistema e a explicação das funcionalidades no vídeo abaixo:

[![Assista ao vídeo de apresentação](https://img.youtube.com/vi/63iN5H-n3q4/0.jpg)](https://youtu.be/63iN5H-n3q4)

> *Clique na imagem acima ou [neste link](https://youtu.be/63iN5H-n3q4) para assistir.*

## 🚀 Funcionalidades Principais

### 🔒 Autenticação e Segurança
* **Login e Cadastro:** Sistema de registro com opção de conta "Administrador" ou "Usuário Comum".
* **Controle de Acesso (ACL):**
    * **Administradores:** Acesso total (Criar, Ler, Editar, Excluir).
    * **Usuários Comuns:** Acesso apenas para visualização e cadastro básico (sem permissão de excluir registros sensíveis).
* **Proteção de Rotas:** Bloqueio de URLs para usuários não logados.

### 📋 Módulos de Gerenciamento (CRUD)
* **Tutores:** Cadastro completo de clientes.
* **Animais:** Ficha do paciente com vínculo ao tutor.
* **Equipe Médica:** Cadastro de veterinários, CRMV e especialidades.
* **Serviços:** Tabela de preços e tipos de atendimento.
* **Agendamentos:** Marcação de consultas integrando *Animal + Veterinário + Serviço*.

---

## 🛠 Tecnologias Utilizadas
* **Backend:** Python 3.12+ & Django 5
* **Frontend:** HTML5, CSS3, GEMINI 3 Pro & Bootstrap 5 (Ícones: Bootstrap Icons)
* **Banco de Dados:** SQLite3
* **Versionamento:** Git & GitHub

---

## 📦 Guia de Instalação e Execução

Siga os passos abaixo de acordo com o seu sistema operacional.

### 1. Clonar o Repositório
Primeiro, baixe o código para sua máquina:


git clone [https://github.com/SEU_USUARIO/clinica-vet.git](https://github.com/SEU_USUARIO/clinica-vet.git)
cd clinica-vet

### 2. Configurar o Ambiente Virtual
🪟 No Windows:
PowerShell

# Cria o ambiente virtual
python -m venv venv

# Ativa o ambiente
.\venv\Scripts\activate


🐧 No Linux ou macOS:
Bash

# Cria o ambiente virtual
python3 -m venv venv

# Ativa o ambiente
source venv/bin/activate

(Após ativar, você deve ver (venv) no início da linha do terminal).

### 3. Instalar Dependências
Com o ambiente ativo, instale as bibliotecas necessárias:

Bash

pip install -r requirements.txt
(Caso não tenha o arquivo requirements.txt, instale o Django manualmente: pip install django).

### 4. Configurar o Banco de Dados
Prepare o banco de dados inicial:

Bash

python manage.py migrate

### 5. Criar um Superusuário (Opcional)
Para ter acesso total desde o início, crie um superusuário:

Bash

python manage.py createsuperuser
(Siga as instruções na tela para definir usuário e senha).

### 6. Iniciar o Sistema 🚀
Agora é só rodar o servidor:

Bash

python manage.py runserver
Acesse no seu navegador: http://127.0.0.1:8000/
