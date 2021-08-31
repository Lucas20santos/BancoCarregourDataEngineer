# LISTA

lista = [1, 2, 3, 4]
lista_animal = ['cachorro', 'gato', 'elefante']

# acessando os elementos das listas 
# a numeração ou index de cada elemento começa 
# a partir do zero

print(lista_animal[0])
print(lista_animal[1])
print(lista_animal[2])

# pode ser usado um laço de repetição para acessar os 
# elementos
soma = 0

for x in lista:
    print(x)
    soma += x

print(soma)
print("Maior valor da lista: ", max(lista))
print(max(lista_animal))

if 'gato' in lista_animal:
    print("existe um gato na lista")
else:
    print("não existe um gato na lista")

## incluindo elementos com o método append()
lista_animal.append("lobo")
print(lista_animal)
## elemento incluido na ultima posição

## removendo elementos com o método pop()
lista_animal.pop(0)
print(lista_animal)
## primeiro elemento foi removido

## ordenar a lista animal com método sort()
lista_animal.sort()
print(lista_animal)
## saída será a lista ordenada alfabetica

## reverter o ordenamento com método reverse
lista_animal.reverse()
print(lista_animal)

# TUPLA

## Declaração de uma tupla pode ser feita ao invés de
## concheite é usado parâtese
tupla = (1, 3, 5, 6)

print(tupla)

## converter uma lista para uma tupla
tupla_animal = tuple(lista_animal)
print(tupla_animal)
