import requests
import json

base_url = 'http://192.168.2.161:8080/api/v1/additionals'
headers = {'Content-Type': 'application/json'}

# Lista de dados para enviar em cada solicitação
data_list = [
    {"category": 1, "name": "Catupiry", "price": 1, "qntd": 0},
    {"category": 1, "name": "Cheddar", "price": 1, "qntd": 0},
    {"category": 1, "name": "Mussarela", "price": 1, "qntd": 0},
    {"category": 1, "name": "Presunto", "price": 1, "qntd": 0},
    {"category": 1, "name": "Ovo", "price": 1, "qntd": 0},
    {"category": 1, "name": "Frango Desfiado", "price": 1, "qntd": 0},
    {"category": 1, "name": "File De Frango", "price": 1, "qntd": 0},
    {"category": 1, "name": "Lombinho", "price": 1, "qntd": 0},
    {"category": 1, "name": "File Mignon", "price": 1, "qntd": 0},
   
    {"category": 3, "name": "Catupiry", "price": 1, "qntd": 0},
    {"category": 3, "name": "Cheddar", "price": 1, "qntd": 0},
    {"category": 3, "name": "Mussarela", "price": 1, "qntd": 0},
    {"category": 3, "name": "Presunto", "price": 1, "qntd": 0},
    {"category": 3, "name": "Ovo", "price": 1, "qntd": 0},
    {"category": 3, "name": "Frango Desfiado", "price": 1, "qntd": 0},
    {"category": 3, "name": "File De Frango", "price": 1, "qntd": 0},
    {"category": 3, "name": "Lombinho", "price": 1, "qntd": 0},
    {"category": 3, "name": "File Mignon", "price": 1, "qntd": 0},
   
    {"category": 4, "name": "Catupiry", "price": 1, "qntd": 0},
    {"category": 4, "name": "Cheddar", "price": 1, "qntd": 0},
    {"category": 4, "name": "Mussarela", "price": 1, "qntd": 0},
    {"category": 4, "name": "Presunto", "price": 1, "qntd": 0},
    {"category": 4, "name": "Ovo", "price": 1, "qntd": 0},
    {"category": 4, "name": "Frango Desfiado", "price": 1, "qntd": 0},
    {"category": 4, "name": "File De Frango", "price": 1, "qntd": 0},
    {"category": 4, "name": "Lombinho", "price": 1, "qntd": 0},
    {"category": 4, "name": "File Mignon", "price": 1, "qntd": 0},
   
    {"category": 5, "name": "Catupiry", "price": 1, "qntd": 0},
    {"category": 5, "name": "Cheddar", "price": 1, "qntd": 0},
    {"category": 5, "name": "Mussarela", "price": 1, "qntd": 0},
    {"category": 5, "name": "Presunto", "price": 1, "qntd": 0},
    {"category": 5, "name": "Ovo", "price": 1, "qntd": 0},
    {"category": 5, "name": "Frango Desfiado", "price": 1, "qntd": 0},
    {"category": 5, "name": "File De Frango", "price": 1, "qntd": 0},
    {"category": 5, "name": "Lombinho", "price": 1, "qntd": 0},
    {"category": 5, "name": "File Mignon", "price": 1, "qntd": 0},
   
    {"category": 6, "name": "Catupiry", "price": 1, "qntd": 0},
    {"category": 6, "name": "Cheddar", "price": 1, "qntd": 0},
    {"category": 6, "name": "Mussarela", "price": 1, "qntd": 0},
    {"category": 6, "name": "Presunto", "price": 1, "qntd": 0},
    {"category": 6, "name": "Ovo", "price": 1, "qntd": 0},
    {"category": 6, "name": "Frango Desfiado", "price": 1, "qntd": 0},
    {"category": 6, "name": "File De Frango", "price": 1, "qntd": 0},
    {"category": 6, "name": "Lombinho", "price": 1, "qntd": 0},
    {"category": 6, "name": "File Mignon", "price": 1, "qntd": 0},
   
    {"category": 7, "name": "Catupiry", "price": 1, "qntd": 0},
    {"category": 7, "name": "Cheddar", "price": 1, "qntd": 0},
    {"category": 7, "name": "Mussarela", "price": 1, "qntd": 0},
    {"category": 7, "name": "Presunto", "price": 1, "qntd": 0},
    {"category": 7, "name": "Ovo", "price": 1, "qntd": 0},
    {"category": 7, "name": "Frango Desfiado", "price": 1, "qntd": 0},
    {"category": 7, "name": "File De Frango", "price": 1, "qntd": 0},
    {"category": 7, "name": "Lombinho", "price": 1, "qntd": 0},
    {"category": 7, "name": "File Mignon", "price": 1, "qntd": 0},
   
    {"category": 8, "name": "Catupiry", "price": 1, "qntd": 0},
    {"category": 8, "name": "Cheddar", "price": 1, "qntd": 0},
    {"category": 8, "name": "Mussarela", "price": 1, "qntd": 0},
    {"category": 8, "name": "Presunto", "price": 1, "qntd": 0},
    {"category": 8, "name": "Ovo", "price": 1, "qntd": 0},
    {"category": 8, "name": "Frango Desfiado", "price": 1, "qntd": 0},
    {"category": 8, "name": "File De Frango", "price": 1, "qntd": 0},
    {"category": 8, "name": "Lombinho", "price": 1, "qntd": 0},
    {"category": 8, "name": "File Mignon", "price": 1, "qntd": 0},
   
    {"category": 9, "name": "Catupiry", "price": 1, "qntd": 0},
    {"category": 9, "name": "Cheddar", "price": 1, "qntd": 0},
    {"category": 9, "name": "Mussarela", "price": 1, "qntd": 0},
    {"category": 9, "name": "Presunto", "price": 1, "qntd": 0},
    {"category": 9, "name": "Ovo", "price": 1, "qntd": 0},
    {"category": 9, "name": "Frango Desfiado", "price": 1, "qntd": 0},
    {"category": 9, "name": "File De Frango", "price": 1, "qntd": 0},
    {"category": 9, "name": "Lombinho", "price": 1, "qntd": 0},
    {"category": 9, "name": "File Mignon", "price": 1, "qntd": 0},
   
]

for data in data_list:
    response = requests.post(base_url, headers=headers, json=data)
    # response = requests.get(base_url, params=data)  # Se estiver usando GET, pode enviar os dados como parâmetros de consulta

    print('Status Code:', response.status_code)
    print('Resposta:', response.text)
    print('\n---\n')  # Separador entre as respostas
