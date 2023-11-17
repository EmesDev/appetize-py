import requests
import json

base_url = 'http://192.168.2.161:8080/api/v1/products'
headers = {'Content-Type': 'application/json'}

# Lista de dados para enviar em cada solicitação
data_list = [
    {"category": 1,  "description": "pao de brioche, bland de frango empanado, bacon ,queijo prato, molho especial, cebola crisp, salada",  "name": "Chicken Miros",  "price": 32,  "qntd": 0,  "url": ""},
    {"category": 1,  "description": "pao especial, 2 bife bland 150g, cheddar, queijo gorgonzola, bacon, molho especial,cebola crispy, salada",  "name": "Double Miros",  "price": 40,  "qntd": 0,  "url": ""},
    {"category": 1,  "description": "pao especial, bife artesanal de costela 150g, costela desfiada, creme de cheddar, bacon, molho especial",  "name": "Miros Costela Premium",  "price": 42,  "qntd": 0,  "url": ""},
    {"category": 1,  "description": "pao de brioche, bife bland 150g, creme de cheddar, bacon, molho especial, cebola",  "name": "miros artesanal",  "price": 32,  "qntd": 0,  "url": ""},
    {"category": 1,  "description": "ao especial, bife artesanal de costela 120gg, cheddar, bacon, molho bbq, cebola crispy,",  "name": "Miros Costela",  "price": 35,  "qntd": 0,  "url": ""},
    {"category": 1,  "description": "pao especial, 2 bife artesanal, de costela 120gg, provolone, bacon, molho bbq,cebola",  "name": "Miros Double Costela",  "price": 40,  "qntd": 0,  "url": ""},
    {"category": 1,  "description": "pao de brioche, bife bland 150g, creme de cheddar, bacon, couve crispy, salada",  "name": "miros gourmet",  "price": 32,  "qntd": 0,  "url": ""},
    {"category": 1,  "description": "pao de brioche, bife bland 150g, cheddar, bacon, anel de cebola, molho especial, salad",  "name": "miros onion ring",  "price": 32,  "qntd": 0,  "url": ""},
    
    {"category": 2,  "description": "pao, bife, queijo, ovo, bacon, frango, presunto, milho, salada e batata palha",  "name": "Da Casa",  "price": 30,  "qntd": 0,  "url": ""},
    {"category": 2,  "description": "pao, bife, queijo, bacon, frango, presunto, salada, batata e milho",  "name": "Especial",  "price": 28,  "qntd": 0,  "url": ""},
    {"category": 2,  "description": "pão, queijo e presunto",  "name": "Misto Quente",  "price": 10,  "qntd": 0,  "url": ""},
    {"category": 2,  "description": "pão, 2 bifes, 2 queijos, 2 presuntos, frango, bacon, milho, salada, batata e calabresa",  "name": "Tabajara",  "price": 37,  "qntd": 0,  "url": ""},
    {"category": 2,  "description": "pão, 2 bifes, ovo, frango, presunto, queijo, bacon, milho, salada e batata",  "name": "X Tudo",  "price": 32,  "qntd": 0,  "url": ""},

    {"category": 3,  "description": "pão, bife, bacon, salada, batata e milho",  "name": "Bacon Burguer",  "price": 16,  "qntd": 0,  "url": ""},
    {"category": 3,  "description": "pão, bife, ovo, bacon, salada, batata e milho",  "name": "Egg Bacon Burguer",  "price": 20,  "qntd": 0,  "url": ""},
    {"category": 3,  "description": "pão, bife, ovo, salada, batata e milho",  "name": "Egg Burguer",  "price": 15,  "qntd": 0,  "url": ""},
    {"category": 3,  "description": "pão, bife, queijo, bacon, salada, batata e milho",  "name": "X Bacon Burguer",  "price": 20,  "qntd": 0,  "url": ""},
    {"category": 3,  "description": "pão, bife, queijo, salada, batata e milho",  "name": "X Burguer",  "price": 15,  "qntd": 0,  "url": ""},
    {"category": 3,  "description": "pão, bife, ovo,queijo, bacon, salada, batata e milho",  "name": "X Egg Bacon Burguer",  "price": 22,  "qntd": 0,  "url": ""},
    {"category": 3,  "description": "pão, bife, ovo,queijo, salada, batata e milho",  "name": "X Egg Burguer",  "price": 20,  "qntd": 0,  "url": ""},
    {"category": 3,  "description": "pão, bife, salada, batata, milho",  "name": "Hamburguer",  "price": 10,  "qntd": 0,  "url": ""},
    
    {"category": 4,  "description": "pão, frango, bacon, salada, batata e milho",  "name": "Bacon Frango",  "price": 24,  "qntd": 0,  "url": ""},
    {"category": 4,  "description": "pão, frango, ovo, bacon, salada, batata e milho",  "name": "Egg Bacon Frango",  "price": 27,  "qntd": 0,  "url": ""},
    {"category": 4,  "description": "pão, frango,ovo, salada, batata e milho",  "name": "Egg Frango",  "price": 24,  "qntd": 0,  "url": ""},
    {"category": 4,  "description": "pão, frango, salada, batata e milho",  "name": "Frango Simples",  "price": 20,  "qntd": 0,  "url": ""},
    {"category": 4,  "description": "pão, frango, queijo, bacon, salada, batata e milho",  "name": "X Bacon Franco",  "price": 27,  "qntd": 0,  "url": ""},
    {"category": 4,  "description": "pão, frango, ovo, bacon,queijo, salada, batata e milho",  "name": "X Egg Bacon Frango",  "price": 30,  "qntd": 0,  "url": ""},
    {"category": 4,  "description": "pão, frango, queijo, ovo, salada, batata e milho",  "name": "X Egg Frango",  "price": 27,  "qntd": 0,  "url": ""},
    {"category": 4,  "description": "pão, frango,queijo, salada, batata e milho",  "name": "X Frango",  "price": 23,  "qntd": 0,  "url": ""},
    
    {"category": 5,  "description": "pao, frango, queijo,bacon, milho, batata e milho",  "name": "Cachorro Quente Frango Bacon",  "price": 23,  "qntd": 0,  "url": ""},
    {"category": 5,  "description": "pao, frango, queijo, catupiry, milho, batata e milho",  "name": "Cachorro Quente Frango Catupiry",  "price": 22,  "qntd": 0,  "url": ""},
    {"category": 5,  "description": "pao, frango, queijo, milho, batata e milho",  "name": "Cachorro Quente Frango",  "price": 19,  "qntd": 0,  "url": ""},
    {"category": 5,  "description": "pao, salsicha, queijo,bacon, milho, batata e milho",  "name": "Cachorro Quente Salsicha Bacon",  "price": 17,  "qntd": 0,  "url": ""},
    {"category": 5,  "description": "pao, salsicha, queijo,catupiry, milho, batata e milho",  "name": "Cachorro Quente Salsicha Catupiry",  "price": 16,  "qntd": 0,  "url": ""},
    {"category": 5,  "description": "pao, salsicha, queijo, milho, batata e milho",  "name": "Cachorro Quente Salsicha",  "price": 12,  "qntd": 0,  "url": ""},
    
    {"category": 6,  "description": "anel de cebola",  "name": "Anel De Cebola 400g",  "price": 20,  "qntd": 0,  "url": ""},
    {"category": 6,  "description": "batata frita com cheddar e bacon 400g",  "name": "Batata Frita Com Cheddar E Bacon 400g",  "price": 45,  "qntd": 0,  "url": ""},
    {"category": 6,  "description": "file de tilapia 500g acompanha batata frita 400g",  "name": "File De Tilapia 500g",  "price": 80,  "qntd": 0,  "url": ""},
    {"category": 6,  "description": "frango empanado 500g e batata frita 400g",  "name": "Porção Frango Empanado",  "price": 65,  "qntd": 0,  "url": ""},
    
    {"category": 7,  "description": "molho bolonhesa, bacon, calabresa, catupiry, mussarela e cheiro verde",  "name": "Macarrao Bolonhesa",  "price": 29,  "qntd": 0,  "url": ""},
    
    {"category": 8,  "description": "Agua Mineral Com Gas",  "name": "Agua Mineral Com Gas",  "price": 3,  "qntd": 0,  "url": ""},
    {"category": 8,  "description": "Agua Mineral Sem Gas",  "name": "Agua Mineral Sem Gas",  "price": 3,  "qntd": 0,  "url": ""},
    {"category": 8,  "description": "Brahma Latão",  "name": "Brahma Latão",  "price": 7,  "qntd": 0,  "url": ""},
    {"category": 8,  "description": "Cerveja Long Neck Corona",  "name": "Cerveja Long Neck Corona",  "price": 8,  "qntd": 0,  "url": ""},
    {"category": 8,  "description": "Cerveja Long Neck Heineken",  "name": "Cerveja Long Neck Heineken",  "price": 8,  "qntd": 0,  "url": ""},
    {"category": 8,  "description": "Red Bull Lata",  "name": "Red Bull Lata",  "price": 10,  "qntd": 0,  "url": ""},

    {"category": 9,  "description": "Refrigerante 1l",  "name": "Refrigerante 1l",  "price": 10,  "qntd": 0,  "url": ""},
    # {"category": 9,  "description": "substituir",  "name": "substituir",  "price": 12,  "qntd": 0,  "url": ""},

]

for data in data_list:
    response = requests.post(base_url, headers=headers, json=data)
    # response = requests.get(base_url, params=data)  # Se estiver usando GET, pode enviar os dados como parâmetros de consulta

    print('Status Code:', response.status_code)
    print('Resposta:', response.text)
    print('\n---\n')  # Separador entre as respostas
