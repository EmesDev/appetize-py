import requests
import json

base_url = 'http://192.168.0.85:8080/api/v1/products'
headers = {'Content-Type': 'application/json'}

# Lista de dados para enviar em cada solicitação
data_list = [
    {"id": 2,  "visible": False},
    {"id": 5,  "visible": False},
    {"id": 7,  "visible": False},
    {"id": 8,  "visible": False},
    {"id": 9,  "visible": False},
    {"id": 12,  "visible": False},
    {"id": 15,  "visible": False},
    {"id": 16,  "visible": False},
    {"id": 22,  "visible": False},
    {"id": 33,  "visible": False},
    {"id": 40,  "visible": False},
]

for data in data_list:
    response = requests.put(base_url, headers=headers, json=data)
    # response = requests.get(base_url, params=data)  # Se estiver usando GET, pode enviar os dados como parâmetros de consulta

    print('Status Code:', response.status_code)
    print('Resposta:', response.text)
    print('\n')  # Separador entre as respostas
