# n1 = int(input('Digite um valor: '))
# n2 = int(input('Digite um valor: '))
# n3 = int(input('Digite um valor: '))
# n4 = int(input('Digite um valor: '))
# numeros = (n1, n2, n3, n4)
# noves = par = posicao_tres = 0
# numeros_pares = []
# for n in numeros:
#     if n == 9:
#         noves += 1
#     if n == 3:
#         posicao_tres = numeros.index(3) + 1
#     if n % 2 == 0:
#         numeros_pares.append(n)
#         par += 1
# print(numeros)
# if par > 0:
#     print(f'Os números pares são: {numeros_pares}')
# else:
#     print('Não existem pares.')
# print(f'O valor 9 apareceu {noves} vez(es)\nO número três aparece na posição {posicao_tres}\n 'if posicao_tres else print(
#     'Não existem números três'))
num = (int(input('Digite um valor: ')), int(input('Digite um valor: ')), int(input(
    'Digite um valor: ')), int(input('DIgite um valor: ')), int(input('Digite um valor: ')))
print(num)
pares = []
if 9 in num:
    print(f'Existem {num.count(9)} noves.')
else:
    print('Não tem nove.')
if 3 in num:
    print(f'O três está na posição {num.index(3)+1}')
else:
    print('Não tem três.')
for n in num:
    if n % 2 == 0:
        pares.append(n)
print(f'Os números pares são: {pares}')
