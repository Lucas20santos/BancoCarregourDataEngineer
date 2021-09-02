from os import system as linux
linux("clear")

class Error(Exception):
    pass

class InputError(Error):
    def __init__(self, message):
        self.message = message

while True:
    try:
        x = int(input('Entre com uma nota de 0 a 10: '))
        if x < 0 or x > 10:
            raise InputError('Valor fora do intervalo')
        
    except ValueError:
        print("Valor invalido!!!")
    except InputError as ex:
        print(ex)
    else:
        break

print(x)
print("OK")
