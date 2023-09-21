print('-='*5, 'LOJAS BAZINGA', '-='*5)
nome = ''
preco = total = produtos_mil = menor_preco = cont = 0
nome_produto_barato = ''
p = 'S'
while p == 'S':
    nome = str(input('Nome do produto: '))
    preco = float(input('Preço: R$'))
    total += preco
    cont += 1
    if cont == 1 or preco < menor_preco:
        menor_preco = preco
        nome_produto_barato = nome
    if preco >= 1000:
        produtos_mil += 1
    p = str(input('Quer continuar? [S/N]')).upper()
    if p == 'N':
        break
print(
    f'O total gasto foi de {total}R$\n{produtos_mil} produtos custam mais de 1000R$\n{nome_produto_barato} é o nome do produto mais barato.')
print('-='*5, 'FIM DO PROGRAMA', '-='*5)
