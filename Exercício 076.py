listagem = ('Lápis', 1.75, 'Borracha', 2.00, 'Caderno', 15.90, 'Estojo', 25.00, 'Transferidor',
            4.20, 'Compasso', 9.99, 'Mochila', 120.32, 'Canetas', 22.30, 'Livro', 34.90)
print('-'*30)
print(f'{"LISTA DE PREÇOS":^30}')
print('-'*30)
for item in range(0, len(listagem), 2):
    print(f'{listagem[item]:.<25}R$', end='')
    print(f'{listagem[item+1]:>7.2f}')
