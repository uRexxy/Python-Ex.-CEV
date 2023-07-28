soma = 0
cont = 0
for n in range(1, 501, 2):
       if n % 3 == 0:
        cont += 1
        soma += n
print(f'A soma de {cont} números ímpares e divisiveis por tres é de: {soma}')
