matriz = []
dados = []
pares = 0
somaterc = 0
for c in range(1, 10):
    num = int(input(f'Digite um valor para [{c}]: '))
    dados.append(num)
    matriz.append(dados[:])
    dados.clear()
print(matriz[0:3])
print(matriz[3:6])
print(matriz[6:10]) 
