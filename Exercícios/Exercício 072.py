numeros = ('Zero', 'Um', 'Dois', 'Tres', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze',
           'Doze', 'Treze', 'Quatorze', 'Quinze', 'Dezesseis', 'Dezesete', 'Dezoito', 'Dezenove', 'Vinte')
while True:
    n = int(input('Digite um números para ver seu nome por extenso: '))
    if n >= 0 and n <= 20:
        break
    else:
        print('Invalido, tente novamente.')
for c in range(0, len(numeros)):
    if n == c:

        print(numeros[n])
