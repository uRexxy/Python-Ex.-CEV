""" from time import sleep
galera = []
dados = []
count_pessoas = 0
while True:
    dados.append(str(input('Nome: ').strip()))
    dados.append(int(input('Peso: ')))
    galera.append(dados[:])
    count_pessoas += 1
    dados.clear()
    r = str(input('Quer continuar? [S/N] ')).strip()
    if r in 'Nn':
        print('Analisando dados...')
        sleep(1)
        break
for n in galera:
    if n == 0:
        maior = menor = n
    else:
        if n >= galera[0][1]:
            maior = galera[n][1]
            nomemaior = galera[n][0]
        elif n <= galera[1][1]:
            menor = galera[n][1]
            nomemenor = galera[n][0]

print(f'O total de pessoas cadastradas foram: {count_pessoas}\nO maior peso é de {maior:.1f}Kg. Peso de {nomemaior}\nO menor é de {menor:.1f}Kg. Peso de {nomemenor}') """
####################################################
temp = []
princ = []
mai = men = 0
while True:
    temp.append(str(input('Nome: ')))
    temp.append(float(input('Peso: ')))
    if len(princ) == 0:
        mai = men = temp[1]
    else:
        if temp[1] > mai:
            mai = temp[1]
        if temp[1] < men:
            men = temp[1]

    princ.append(temp[:])
    temp.clear()
    resp = str(input('Quer continuar? [S/N]: '))
    if resp in 'Nn':
        break

print('=-'*30)
print(f'Ao todo, você cadastrou {len(princ)} pessoas. ')
print(f'O maior peso foi de {mai}Kg. Peso de ', end='')
for p in princ:
    if p[1] == mai:
        print(f'[{p[0]}] ', end='')
print()
print(f'O menor peso foi de {men}Kg. Peso de ', end='')
for p in princ:
    if p[1] == men:
        print(f'[{p[0]}] ', end='')
print()
