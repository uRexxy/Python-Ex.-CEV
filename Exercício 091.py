from random import randint as ri
from time import sleep
maior = menor = 0
cont = 1

jogos = {}
jogos['Jogador 1'] = ri(1, 6)
jogos['Jogador 2'] = ri(1, 6)
jogos['Jogador 3'] = ri(1, 6)
jogos['Jogador 4'] = ri(1, 6)
print('Valores sorteados:')
for k, n in jogos.items():
    print(f'\tO {k} tirou {n}')
    sleep(1)
print('Ranking dos jogadores:')
jogos_ordem = sorted(jogos.items(), reverse=True)
for k, n in jogos_ordem:
    print(f'\t{cont}°. {k} com {n}')
    cont += 1
    sleep(1)
