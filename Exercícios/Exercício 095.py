# from time import sleep

# jogadores = []
# n = 1

# while True:
#     dados = {}  # Criei um novo dicionário 'dados' a cada iteração do loop
#     dados["Nome"] = str(input('Nome do jogador: ')).capitalize()
#     partidas = int(input('Quantas partidas ele jogou? '))

#     gols = []
#     total = 0
#     for cont in range(partidas):
#         gol = int(input(f'Quantos gols na {cont + 1}° partida? '))
#         gols.append(gol)
#         total += gol

#     dados["Gols"] = gols
#     dados["Total"] = total

#     jogadores.append(dados.copy())

#     r = str(input('Quer continuar? [S/N]: ')).upper()
#     if r == 'N':
#         print('Analisando dados...')
#         sleep(1)
#         print('-=' * 20)
#         break

# print('-' * 40)
# for k, j in enumerate(jogadores):
#     print(f'{n} {jogadores[k]}')
#     n += 1
# print('-'*40)
# while True:
#     resp = int(input('Mostrar dados de qual jogador? '))
#     for k, j in enumerate(jogadores):
#         if k == resp:
#             print(f'\t-levantamento do jogador {jogadores[k]["Nome"]}:')
#             for cont in range(partidas):
#                 print(f'No jogo {cont+1} fez {j["Gols"][cont]}')


from time import sleep

jogadores = []
n = 1

while True:
    dados = {}
    dados["Nome"] = str(input('Nome do jogador: ')).capitalize()
    partidas = int(input('Quantas partidas ele jogou? '))

    gols = []
    total = 0
    for cont in range(partidas):
        gol = int(input(f'Quantos gols na {cont + 1}° partida? '))
        gols.append(gol)
        total += gol

    dados["Gols"] = gols
    dados["Total"] = total

    jogadores.append(dados.copy())

    r = str(input('Quer continuar? [S/N]: ')).upper()
    if r == 'N':
        print('Analisando dados...')
        sleep(1)
        print('-=' * 20)
        break

print('-' * 40)
for k, j in enumerate(jogadores):
    print(f'{n} {jogadores[k]}')
    n += 1
print('-' * 40)

while True:
    resp = int(input('Mostrar dados de qual jogador? (0 para sair) ')) - 1
    if resp == -1:
        print('Saindo...')
        break
    if 0 <= resp < len(jogadores):
        print(f'\t- Levantamento do jogador {jogadores[resp]["Nome"]}:')
        for cont, gol in enumerate(jogadores[resp]["Gols"]):
            print(f'\tNo jogo {cont + 1} fez {gol} gols')
    else:
        print('Jogador não encontrado. Tente novamente.')
