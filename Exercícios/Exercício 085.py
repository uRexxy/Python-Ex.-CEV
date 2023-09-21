numeros = []
impares = []
pares = []
for n in range(1, 8):
    num = int(input(f'Digite o {n}o número: '))
    if num % 2 == 0:
        pares.append(num)
    else:
        impares.append(num)
numeros.append(pares[:])
numeros.append(impares[:])
print(
    f'Os números ímpares são {sorted(impares)} e os números pares são {sorted(pares)}')
