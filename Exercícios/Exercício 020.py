from random import shuffle
n1 = str(input('Primeiro noob: '))
n2 = str(input('Segundo nome: '))
n3 = str(input('Terceiro nome:'))
n4 = str(input('Quarto nome: '))
noobs = [n1, n2, n3, n4]
shuffle(noobs)
print(f'A ordem do maior noobao está da esquerda para a direita! {noobs}')