import hashlib
from os import system as linux

linux("clear")

arquivo1 = "arquivo3.txt"
arquivo2 = "arquivo4.txt"

hash1 = hashlib.new('ripemd160')
hash1.update(open(arquivo1, 'rb').read())


hash2 = hashlib.new('ripemd160')
hash2.update(open(arquivo2, 'rb').read())

if hash1.digest()!= hash2.digest():
    print("Os arquivos são diferentes")
else:
    print("Os arquivos são iguais")

print("Hash arquivo1: ", hash1.hexdigest())
print("Hash arquivo2: ", hash2.hexdigest())
