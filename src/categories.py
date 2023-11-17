import requests
import json

base_url = 'http://192.168.2.161:8080/api/v1/categories'
headers = {'Content-Type': 'application/json'}

# Lista de dados para enviar em cada solicitação
data_list = [
    {
        "name": "Artesanais",
        "visible": True
    },
    {
        "name": "Especiais",
        "visible": True
    },
    {
        "name": "Hamburguer",
        "visible": True
    },
    {
        "name": "Frango",
        "visible": True
    },
    {
        "name": "Cachorro Quente",
        "visible": True
    },
    {
        "name": "Entradas",
        "visible": True
    },
    {
        "name": "Massas",
        "visible": True
    },
    {
        "name": "Outras Bebidas",
        "visible": True
    },
    {
        "name": "Refrigerante 1l",
        "visible": True
    }
    # Adicione mais conjuntos de dados conforme necessário
]

for data in data_list:
    response = requests.post(base_url, headers=headers, json=data)
    # response = requests.get(base_url, params=data)  # Se estiver usando GET, pode enviar os dados como parâmetros de consulta

    print('Status Code:', response.status_code)
    print('Resposta:', response.text)
    print('\n---\n')  # Separador entre as respostas
