numeros = []
r = ''
while True:
    if r == 'N':
        break
    num = input('Digite um valor: ')
    if num.isnumeric():
        int(num)
        if num not in numeros:
            numeros.append(num)
            print('Valor adicionado com sucesso!')
        else:
            print('Esse número ja foi digitado. Tente denovo!')
        r = str(input('Quer continuar? [S/N] ')).strip().upper()
    else:
        print('Erro! Previsa ser inteiro.')
print(f'Os valores digitados são: {sorted(numeros)}')
