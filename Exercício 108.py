import utilidadesCeV.moeda as moeda

n = float(input('Digite o preço: R$'))
print(f'A metade de {moeda.monetario(n)} é {moeda.monetario(moeda.metade(n))}')
print(f'O dobro de {moeda.monetario(n)} é {moeda.monetario(moeda.dobro(n))}')
print(f'Aumentando 10%, temos {moeda.monetario(moeda.aumentar(n, 10))}')
print(f'Diminuindo 13%, temos {moeda.monetario(moeda.diminuir(n, 13))}')
