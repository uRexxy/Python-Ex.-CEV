from random import sample
from time import sleep
jogos = []
dados_jogos = []
print('=-='*10, 'Gerador de jogos Mega Sena', '=-='*10)
quantidade_jogos = int(input('Quantos jogos deseja gerar? '))
cont = 0
n = 1
while True:
    dados_jogos.append(sample(range(1, 60), 6))
    jogos.append(dados_jogos[:])
    dados_jogos.clear()
    cont += 1
    if cont == quantidade_jogos:
        break
print('Gerando valores...')
sleep(1)
for j in jogos:
    print(f'Jogo {n}:\n{j}')
    print()
    sleep(1)
    n += 1
