v = int(input('Qual a velocidade do carro? '))
multa = 0
if v > 80:
    print('Você foi multado!')
    multa = (v - 80) * 7
    print(f'Sua multa é de R${multa:.2f}')
else:
    print('Não foi multado.')
