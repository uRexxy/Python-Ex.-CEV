soma = 0
somaimp = 0
for i in range(1, 7):
    n = int(input('Digite um número inteiro: '))
    if n % 2 == 0:
        soma += n
    if n % 2 != 0:
        somaimp += n
print(f'A soma dos números pares é: {soma}')
print(f'A soma dos números ímpares é: {somaimp}')
