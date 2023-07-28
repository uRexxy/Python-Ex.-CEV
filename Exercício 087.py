matriz = []
dados = []
pares = 0
somaterc = 0
for c in range(1, 10):
    num = int(input(f'Digite um valor para [{c}]: '))
    dados.append(num)
    matriz.append(dados[:])
    dados.clear()
    if num % 2 == 0:
        pares += num
for n in range(1, 10, 2):
    somaterc += matriz[n]
maiorsec = max(matriz[3:6])
print(matriz[0:3])
print(matriz[3:6])
print(matriz[6:10])
print(f'A soma dos números pares é {pares}.' if pares > 0 else print('Não tem pares.'))
print(f'A soma dos valores da terceira coluna é {somaterc}')####################################################
print(f'O maior valor da coluna 2 é: {maiorsec}')