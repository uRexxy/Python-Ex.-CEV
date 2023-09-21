numeros = []
n = digitos = 0
r = ''
while True:
    n = int(input('Digite um valor: '))
    r = str(input('Quer continuar? [S/N] ')).strip().upper()
    numeros.append(n)
    digitos += 1
    if r == 'N':
        break
    if n == 5:
        cinco_lista = True
        posicao_cinco = numeros.index(5)
    else:
        cinco_lista = False
print('=-='*20)
print(f'A lista em forma decresente: {sorted(numeros, reverse=True)}')
print(f'Foram digitados {digitos} valores.')
print(f'O valor 5 está na lista na posição {posicao_cinco}' if cinco_lista ==
      True else 'O valor 5 não está na lista.')
