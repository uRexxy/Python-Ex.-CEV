import utilidadesCeV.moeda as moeda

n = float(input('Digite o preço: R$'))
print(f'A metade de {n} é {moeda.metade(n):.2f}')
print(f'O dobro de {n} é {moeda.dobro(n):.2f}')
print(f'Aumentando 10%, temos {moeda.aumentar(n, 10):.2f}')
print(f'Diminuindo 13%, temos {moeda.diminuir(n, 13):.2f}')
