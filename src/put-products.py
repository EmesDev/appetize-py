import requests
import json

base_url = 'http://192.168.2.161:8080/api/v1/products'
headers = {'Content-Type': 'application/json'}

# Lista de dados para enviar em cada solicitação
data_list = [
    # {"category": 1,  "description": "Pão, Salada, Bife, Salada, Bacon",  "name": "X bacon",  "price": 16,  "qntd": 0,  "url": "dawd"},
    {"category": 1, "id": 2,  "description": "Pão, Salada, Bife, Salada, Bacon",  "name": "X Salada",  "price": 12,  "qntd": 0,  "url": "dawd", "visible": False},
    {"category": 1, "id": 3, "description": "Pão, Salada, Bife, Salada, Bacon",  "name": "X Zunto",  "price": 18,  "qntd": 0,  "url": "dawd", "visible": True},
    # {"category": 2,  "description": "Hamburguer com bacon",  "name": "X bacon",  "price": 16,  "qntd": 0,  "url": "string"},
]

for data in data_list:
    response = requests.put(base_url, headers=headers, json=data)
    # response = requests.get(base_url, params=data)  # Se estiver usando GET, pode enviar os dados como parâmetros de consulta

    print('Status Code:', response.status_code)
    print('Resposta:', response.text)
    print('\n')  # Separador entre as respostas
