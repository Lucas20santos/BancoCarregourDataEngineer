from time import sleep
from threading import Thread
from os import system as linux
linux("clear")


def carro(velocidade, piloto):
    trajeto = 0
    while trajeto <= 100:
        trajeto += velocidade
        sleep(0.5)
        print(f"{piloto} - {trajeto} ")

t_carro1 = Thread(target=carro, args=[1, "Bruno"])
t_carro2 = Thread(target=carro, args=[2, "Lucas"])

t_carro1.start()
t_carro2.start()

