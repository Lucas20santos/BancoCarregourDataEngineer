import ipaddress as IP
from os import system as linux
linux("clear")

ip = '192.168.0.100'

endereco = IP.ip_address(ip)
rede = IP.ip_network(ip)

print(f"rede: {rede}")
