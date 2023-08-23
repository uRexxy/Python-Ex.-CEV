total = float(input('Valor total das compras: R$'))
print('Escolha uma forma de pagamento:')
print("""À vista dinheiro ou cheque: [1]
À vista no cartão: [2]
2x no cartão: [3]
3x ou mais: [4]""")
c = int(input('Sua escolha: '))
if c == 1:
    total = total - ((total * 10) / 100)
    print(f'Você ganhou 10% off, o total agora será de R${total:.2f}')
if c == 2:
    total = total - ((total * 5) / 100)
    print(f'Você ganhou 5% off, o total agora será de R${total:.2f}')
if c == 3:
    total = total / 2
    print(f'O total é de 2x de R${total:.2f}')
if c == 4:
    total = total + ((total * 20) / 100)
    totparc = int(input('Quantas parcelas? '))
    parcela = total / totparc
    print(
        f'3x ou mais de parcelas acompanha com 20% de juros, o total agora será de {totparc}x de ${parcela:.2f}')
else:
    total = 0
    print('OPÇÃO INVALIDA')
