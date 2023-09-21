from time import sleep

dados = {}
gols = []

partida = 0
cont = 1
total = 0

dados["Nome"] = str(input('Qual o nome do jogador? ')).strip()
partidas = int(input('Quantas partidas ele jogou? '))
while cont != partidas + 1:
    gols.append(int(input(f'Quantos gols na {cont}° partida? ')))
    cont += 1
for gol in gols:
    total += gol
dados["Gols"] = gols
dados["Total"] = total
print('-='*20)
print(f'{dados}')
print('-='*20)
print(f'O campo nome tem o valor {dados["Nome"]}.')
print(f'O campo gols tem o valor {dados["Gols"]}.')
print(f'O campo total tem o valor {dados["Total"]}.')
print('-='*20)
print(f'O jogador {dados["Nome"]} jogou {partidas} partidas.')
for k, gol in enumerate(gols):
    if partida < partidas:
        print(f'\t=> Na partida {k+1}, fez {gol} gols.')
        partida += 1
        sleep(1)
