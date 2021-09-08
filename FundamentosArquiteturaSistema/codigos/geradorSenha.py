import random
import string
from os import system as linux
linux("clear")

tamanhoSenha = 20

estruturaSenha = string.ascii_letters + string.digits + '~^çÇ/|\;:°º{[}]´`<>!@#$%&*()?., +=_-'

rnd = random.SystemRandom()

print(''.join(rnd.choice(estruturaSenha) for i in range(tamanhoSenha)))
