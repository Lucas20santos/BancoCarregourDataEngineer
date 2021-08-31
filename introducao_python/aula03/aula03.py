valor1 = 10
valor2 = 10

if valor1 > valor2:
    print(f"{valor1} > {valor2}")
elif valor1 < valor2:
    print(f"{valor1} < {valor2}")
else:
    print(f"{valor1} = {valor2}")

print("Final do Programa!!!")

n3 = 11
n2 = 11

resto1 = n3 % 2
resto2 = n2 % 2

if resto1 == 0 or not resto2 > 0:
    print("Foi digitado um número par")
else:
    print("Não foi digitado um número par")
