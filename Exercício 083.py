n = str(input('Digite uma expressão: '))
for e in n:
    parenteses_aberto = n.count('(')
    parenteses_fechado = n.count(')')
if parenteses_aberto == parenteses_fechado:
    print('Sua expressão está correta!')
else:
    print('Sua expressão está incorreta!')