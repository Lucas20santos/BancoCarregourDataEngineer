import os

a = int(input("Entre com o número: "))

for x in range(1, a + 1):
    print(f"{x:^3}", end=" ")
    if x % 10 == 0 and x != 0:
        print()
print()
