numeros = []
for c in range(0, 5):
    numeros.append(int(input(f'Digite um número ({c}): ')))
print(f'A lista é: {numeros}')
print(
    f'O maior valor é {max(numeros)} e esta nas posições {numeros.index(max(numeros))}')
print(
    f'O menor valor é {min(numeros)} e esta na posição {numeros.index(min(numeros))}')
