n = int(input('Informe um número: '))
print(f'Analisando o número {n}')
uni = n % 10
dez = (n // 10) % 10
cen = (n // 100) % 10
mil = (n // 1000) % 10
print(f'Unidade: {uni}')
print(f'Dezena: {dez}')
print(f'Centena: {cen}')
print(f'Milhar: {mil}')
