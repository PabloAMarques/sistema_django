# Emprestimo Bancario Django

## Requisitos

Certifique-se de que você tem os seguintes requisitos instalados em sua máquina:

- Python 3.8

## Configuração do Ambiente Virtual

Recomendo o uso de um ambiente virtual para isolar as dependências do seu projeto. Siga estas etapas para configurar o ambiente virtual:

1. Abra um terminal.

2. Navegue até o diretório do seu projeto:
   "cd /caminho/para/seu/projeto"

3.  De este comando para criar a venv e ativar a venv:
    "python -m venv venv"
    "venv\Scripts\activate"

4. Execute este comando para instalar as dependencias:
    "pip install -r requirements.txt"

5. Aplique as migrações do Django para configurar o banco de dados:
    "python manage.py migrate"

6. Inicie o servidor de desenvolvimento do Django: # O servidor estará disponível em http://127.0.0.1:8000/ por padrão.
    "python manage.py runserver"

7. Você pode acessar o painel de administração em http://127.0.0.1:8000/admin/. Para criar um superusuário, execute o seguinte comando:
    "python manage.py createsuperuser"