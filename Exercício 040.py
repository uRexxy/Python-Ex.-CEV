n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
m = (n1 + n2) / 2
print(f'Sua média foi de {m}')
if m >= 7:
    print('Você foi aprovado!')
elif 7 > m >= 5:
    print('Você está de recuperação!')
else:
    print('Você foi reprovado!')
