import socket
import os

os.system("clear")

try:
    con = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
except socket.error as e:
    print(f"falha: {e}")
else:
    print("sucesso!!!")


host = "localhost"
port = 5434

con.bind((host, port))
msn = "Servidor: Olá tudo de boa?"

print("ok")


while 1:
    dados, end = con.recvfrom(4096)

    if dados:
        print("Servidor enviando mensagens")
        con.sendto(dados + (msn.encode()), end)
