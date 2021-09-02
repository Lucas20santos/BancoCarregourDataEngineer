from os import system as linux
linux("clear")

lista = [1, 2]

try:
    # divisao = 10 / 0
    numero = lista[0]
except ZeroDivisionError:
    print("Não é possível realizar uma divisão por zero")
except IndexError:
    print("Erro ao acessar um indice inválido da lista")
except BaseException as ex:
    print(ex)
else:
    print("Executa quando não ocorrer exceção")
finally:
    print("OK")