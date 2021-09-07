import socket
import os
os.system("clear")

try:
    con = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
except socket.error as e:
    print(f"Falha!!! \nErro: {e}")
else:
    print("sucesso!!!")

host = "localhost"
port = 5433
msn = "Hello World!!!"

print("ok")

try:
    print(f"Cliente: {msn}")
    con.sendto(msn.encode(), (host, port))

    dados, servidor = con.recvfrom(4096)
    dados = dados.decode()
    print(f"Cliente: {dados}")
except socket.error as e:
    print(e)
finally:
    print("close to conection")
    con.close()
