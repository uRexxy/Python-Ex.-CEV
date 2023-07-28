primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
termo = primeiro
cont = 1
while cont <= 10:
    cont += 1
    print(termo, end=' > ')
    termo += razao
print('FIM')
