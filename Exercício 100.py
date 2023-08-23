from random import randint
from time import sleep

valores = []


def sorteia():
    valores.append(randint(0, 10))
    valores.append(randint(0, 10))
    valores.append(randint(0, 10))
    valores.append(randint(0, 10))
    valores.append(randint(0, 10))
    print('Sorteando 5 valores da lista:', end=' ')

    for valor in valores:
        print(valor, end=' ', flush=True)
        sleep(0.3)
    print('PRONTO!')


def somaPar():
    somapar = 0
    for n in valores:
        if n % 2 == 0:
            somapar += n
    print(f'Somando os valores pares de {valores} temos {somapar}')


sorteia()
somaPar()
