from math import factorial
n = int(input('Digite um número para ver seu fatorial: '))
fat = 0
for i in range(n, 0, -1):
    fat = factorial(n)
    print(f'{i} x ', end='')
print(f'O fatorial de {n} é: {fat}')
