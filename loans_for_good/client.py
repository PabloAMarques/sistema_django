import requests
import json

# Dados da proposta em formato de dicionário
proposal_data = {
    "document": "123456789",
    "name": "John Doe"
}

# Converter os dados para JSON
json_data = json.dumps(proposal_data)

# Definir os cabeçalhos apropriados
headers = {
    "Content-Type": "application/json",
}

# Enviar a solicitação POST com os dados em JSON
response = requests.post("http://127.0.0.1:8000/create-proposal-page/", data=json_data, headers=headers)

# Verificar a resposta
if response.status_code == 201:
    print("Proposta enviada com sucesso!")
    proposal = response.json()
    print("ID da Proposta:", proposal["id"])
    print("Aprovação:", proposal["approved"])
else:
    print("Falha ao enviar a proposta. Código de status:", response.status_code)
