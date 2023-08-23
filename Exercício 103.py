def ficha(nome=' ', gols=0):
    nome = str(input('Nome do Jogador: '))
    gols = input('Número de Gols: ')
    if gols.isdigit():
        gols = int(gols)
    else:
        gols = 0

    if nome.strip() == '':
        nome = '<desconhecido>'

    if gols is False:
        gols = 0
    print(f'O jogador {nome} fez {gols} gol(s) no campeonato')


ficha()
