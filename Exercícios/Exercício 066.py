n = s = c = 0
while True:
    n = int(input('Digite um Número: (999 para parar) '))
    if n == 999:
        break
    c += 1
    s += n
print(f'A soma de {c} valores é de {s}')
