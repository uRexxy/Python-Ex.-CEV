casa = float(input('Qual o valor da casa? R$'))
salario = float(input('Quanto você ganha por mês? R$'))
anos = int(input('Em quantos anos você deseja quitar a casa? '))
meses = anos * 12
prestacao = meses / salario
limite = 0.3
limite = salario * limite
if limite > salario:
    print('Não será possível fazer o financiamento.')
else:
    print('O financiamento será possível!')
