numeros = []
pares = []
impares = []

while True:
    numeros.append(int(input('Digite um valor: ')))
    r = str(input('Quer continuar? '))

    if r == 'N':
        break
for n in numeros:
    if n % 2 == 0:
        pares.append(n)
    else:
        impares.append(n)
print('=-='*15)
print(f'A lista completa é: {sorted(numeros)}\nOs números pares são: {sorted(pares)}\nOs números ímpares são: {sorted(impares)}')
