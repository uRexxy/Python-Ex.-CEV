pesos = []
for p in range(1, 6):
    pesosp = float(input(f'Digite o peso da {p}ᵅ pessoa: '))
    pesos.append(pesosp)
maior = max(pesos)
menor = min(pesos)
print(f'O menor peso é: {menor}Kg\n O maior peso é: {maior}Kg')
