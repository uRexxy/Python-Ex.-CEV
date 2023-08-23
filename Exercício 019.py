from random import choice

n1 = str(input('Primeiro nome: '))
n2 = str(input('Segundo nome: '))
n3 = str(input('Terceiro nome: '))
n4 = str(input('Quarto nome: '))
nome_s = choice([n1, n2, n3, n4])
print(f'O nome sorteado foi: {nome_s}')