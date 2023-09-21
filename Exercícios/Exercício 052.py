n = int(input('Digite um número para ver se ele é primo: '))
tot = 0
for i in range(1, n + 1):
    if n % i == 0:
        print('\033[33m', end=' ')
        tot += 1
    else:
        print('\033[31m', end=' ')
    print(i, end=' ')
print(f'\nO número foi dividido {tot} vezes')
if tot == 2:
    print('É um número primo!')
else:
    print('Não é um número primo!')
# NÃO CONSEGUI
