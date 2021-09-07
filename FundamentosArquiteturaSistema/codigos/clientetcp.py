import socket
import sys
import os

os.system("clear")

def main():
    try:
        con = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
    except socket.error as erro:
        print(f"Falha na criação do socket: {erro}")
        sys.exit()
    else:
        print("Socket criado com sucesso!!!")


    hostAlvo = input("Digite o hoste ou ip: ")
    portAlvo = input("Informe a porta para conecção: ")


    try:
        con.connect((hostAlvo, int(portAlvo)))
        con.shutdown(2)
    except socket.error as e:
        print(f"erro na conecção: {e}")
        sys.exit()
    else:
        print("Sucesso!!!")
        

if __name__ == "__main__":
    main()
