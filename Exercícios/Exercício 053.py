frase = str(input('Digite uma frase: ')).replace(' ', '').upper()
frasein = frase[::-1]
if frase == frasein:
    print('É um palíndromo!')
else:
    print('Não é um palíndromo!')
print(f'O inverso de {frase} é {frasein}')