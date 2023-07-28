from time import sleep
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

print(
    f'O total de pessoas cadastradas foram: {count_pessoas}\nO maior peso é de {maior:.1f}Kg. Peso de {nomemaior}\nO menor é de {menor:.1f}Kg. Peso de {nomemenor}')
####################################################