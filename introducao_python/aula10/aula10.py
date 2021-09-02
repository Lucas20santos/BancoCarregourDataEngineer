from datetime import date, time, datetime, timedelta
from os import system as linux

linux("clear")

def trabalhandoComDate():

    data_atual = date.today()
    print(data_atual.strftime('%d - %m - %y'))
    print(data_atual.strftime('%A - %B - %Y'))

def trabalhoandoComTime():
    # pode criar horarios
    horario = time(hour=15, minute=30, second=20)
    #imprimindo o horario e formatando
    print(horario.strftime('%H: %M: %S'))

def trabalhandoComDatetime():
    dataAtual = datetime.now()
    print(dataAtual)
    print(dataAtual.strftime('%d/%m/%Y %H:%M:%S'))
    print(dataAtual.strftime('%c'))
    print(dataAtual.weekday())
    tuplaDias = ('Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sábado', 'Domingo')
    print(tuplaDias[dataAtual.weekday()])
    data_string = '01/01/2029'
    data_convertida = datetime.strptime(data_string, '%d/%m/%Y %H:%M:%S')
    nova_data = data_convertida - timedelta(days=365, hours=3, weeks= 4)
    print(nova_data)


print("Trabalhando com DATE: ")
trabalhandoComDate()

print(" ")
print("Trabalhando com o TIME: ")
trabalhoandoComTime()

print(" ")
print("Trabalhando com DATETIME")
trabalhandoComDatetime()
