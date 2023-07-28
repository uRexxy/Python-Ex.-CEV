media = menor = maior = cont = 0
p = 'S'
numeros = []
while p == 'S':
    n = int(input('Digite um número: '))
    cont += 1
    media += n
    numeros.append(n)
    p = str(input('Quer continuar? [S/N] ')).upper()
maior = max(numeros)
menor = min(numeros)
mfinal = media / cont
print(f'Voce digitou {cont} números e a média foi {mfinal}', end='. ')
print(f'O maior valor digitado foi {maior} e o menor valor foi {menor}')
