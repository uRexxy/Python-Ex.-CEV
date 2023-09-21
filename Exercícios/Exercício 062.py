print('Gerador de PA')
print('-'*18)
while True:
    primeiro = int(input('Primeiro termo: '))
    razao = int(input('Razão: '))
    termo = primeiro
    cont = 1
    while cont <= 10:
        cont += 1
        print(termo, end=' > ')
        termo += razao
    r = str(input('Quer continuar? [S/N]')).strip().upper()
    if r == 'N':
        break
print('FIM')
