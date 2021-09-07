from os import system as linux
import os

def pingPython():
    ip_host = input("Digite o IP ou Host: ")

    linux("ping -n 6 " + ip_host)


def acessarArquivo(nomeArquivo):
    with open(nomeArquivo) as file:
        dump = file.read()

    return dump.splitlines()


def pingMultiplos():
    linux("clear")

    arquivo = acessarArquivo("host.txt")
    
    for ip in arquivo:
        linux("ping -c 4 " + ip)
        print("# " * 20)
        

pingMultiplos()
