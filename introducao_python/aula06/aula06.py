# criando um conjunto
conjunto1 = {1, 2, 3, 4, 6}
print(conjunto1)

## conjunto não permite duplicidade
conjunto2 = {1, 2, 2, 3, 4, 5, 5}
print(conjunto2)

## conjunto união
conjunto_uniao = conjunto1.union(conjunto2)
print(conjunto_uniao)

## conjunto intersecção
conjunto_interseccao = conjunto1.intersection(conjunto2)
print(conjunto_interseccao)

# conjunto diferênca a ordem faz importa
conjuntoD1 = conjunto1.difference(conjunto2)
print(conjuntoD1)
conjuntoD2 = conjunto2.difference(conjunto1)
print(conjuntoD2)

## diferencia simetrica é tudo que 
# não tem nos dois
conjunto_diff_simetrico = conjunto2.symmetric_difference(conjunto1)
print(conjunto_diff_simetrico)
