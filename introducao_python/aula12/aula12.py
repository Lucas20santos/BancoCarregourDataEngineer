import requests
from os import system as linux
linux("clear")

# O que são pacotes
# O que é o instalador de pacotes do Python (PIP)
# Como instalar um pacote no Python
# Como listar pacotes instalador no Python
# COmo utilizar um pacote 
# Instalar nosso primeiro pacote(Requests)
# Realizar uma requisão http com requests

r = requests.get('https://viacep.com.br/ws/51010060/json/', auth=('user', 'pass'))
print(r.status_code)
print(r.json())
dados = r.json()
print(dados['logradouro'])
