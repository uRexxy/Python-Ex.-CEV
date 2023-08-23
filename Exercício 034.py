s = float(input('Qual é seu salário? '))
if s <= 1250:
    novo = s + (s * 15 / 100)
else:
    novo = s + (s * 10 / 100)
print(f'Quem ganhava R${s:.2f}, passa a ganhar R${novo:.2f} agora.')
