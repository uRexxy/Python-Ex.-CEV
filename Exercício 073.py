clubes = ('Botafogo', 'Flamengo', 'Grêmio', 'Fluminense',
           'Palmeiras', 'Bragantino', 'Fortaleza', 'São Paulo',
             'Cruzeiro', 'Internacional',
          'Athletico-PR', 'Atlético-MG', 'Santos', 'Cuiabá',
            'Corinthians', 'Bahia', 'Goiás', 'Coritiba',
              'Vasco da Gama', 'América-MG')
print('OS 5 PRIMEIROS:')
print(clubes[0:5])
print('='*50)
print('OS 4 ÚLTIMOS:')
print(clubes[16:])
print('='*50)
print('EM ORDEM ALFABÉTICA:')
print(sorted(clubes))
print('='*50)
print('POSIÇÃO DO VASCO DA GAMA:')
for time in clubes:
    if time == 'Vasco da Gama':
        posicaovasco = clubes.index('Vasco da Gama') + 1
        print(f'O Vasco da Gama está na posição {posicaovasco} da tabela')
