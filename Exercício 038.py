print('-'*5, 'MAIOR OU MENOR', '-'*5)
n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro valor: '))
if n1 > n2:
    print('O primeiro valor é maior!')
elif n2 > n1:
    print('O segundo valor é maior!')
elif n1 == n2:
    print('Os valores são iguais')
