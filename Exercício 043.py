print('='*5, 'Calculadora IMC', '='*5)
peso = float(input('Qual o seu peso em kg? '))
altura = float(input('Qual a sua altura em metros? '))
imc = peso / (altura ** 2)
print(f'Um IMC de {imc:.1f} é: ', end='')
if imc < 18.5:
    print('Abaixo do peso.')
elif imc <= 25:
    print('Peso ideal')
elif imc <= 30:
    print('Sobrepeso')
elif imc <= 40:
    print('Obesidade')
elif imc > 40:
    print('Obesidade mórbida')
