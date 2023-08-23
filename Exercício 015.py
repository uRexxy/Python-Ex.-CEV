km_rodados = int(input('Quantos KM rodados? KM'))
dias = int(input('Por quantos dias? '))
total = (dias * 60) + (km_rodados * 0.15)
print(f'O valor a ser pago é R${total:.2f}')
