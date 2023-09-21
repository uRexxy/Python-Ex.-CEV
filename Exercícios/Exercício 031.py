v = float(input('Qual a distância da sua viagem? '))
if v <= 200:
    v1 = v * 0.50

else:
    v1 = v * 0.45
print(f'O preço da sua passagem será de R${v1:.2f}')
