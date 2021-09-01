# funções anonimas
lista = ['lucas', 'camila', 'vitoria', 'antonio', 'marcus'
'vinicius', 'fernanda', 'joana']

contador_letra = lambda lista: [len(x) for x in lista]

print(contador_letra(lista))

calculadora = {
    'soma' : lambda a, b: a + b,
    'subtracao': lambda a, b: a - b,
    'multiplicacao': lambda a, b: a * b,
}

print(soma(5, 6))
