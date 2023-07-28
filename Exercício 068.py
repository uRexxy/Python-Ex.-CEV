import random
print('-='*15)
print('VAMOS JOGAR PAR OU ÍMPAR')
print('-='*15)
n = vitoria = 0
while True:
    n = int(input('Diga um valor: '))
    chute = str(input('Par ou Ímpar? [P/I] ')).upper()
    maquina = random.randint(1, 10)
    resultado = n + maquina
    print('-'*30)
    print(f'Voce jogou {n} e o computador jogou {maquina}. Total de {n+maquina}', end=' ')
    print('DEU PAR' if resultado % 2 == 0 else 'DEU ÍMPAR')
    print('-'*30)
    if resultado % 2 == 0 and chute == 'P':
        vitoria += 1
        print('Voce VENCEU!\nVamos jogar novamente...')
    elif resultado % 2 != 0 and chute == 'I':
        vitoria += 1
        print('Voce VENCEU!\nVamos jogar novamente...')
    else:
        print('Voce PERDEU!')
        break
    print('-='*15)
print(f'Voce venceu {vitoria} vezes.')
