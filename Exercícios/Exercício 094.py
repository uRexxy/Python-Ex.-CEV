from time import sleep
pessoas = []
pessoa = {}

idade_acima = []
mulheres = []
idades = []
media = 0
soma_idades = 0
cadastros = 0
while True:
    pessoa["Nome"] = str(input('Nome: '))
    pessoa["Idade"] = int(input('Idade: '))
    pessoa["Sexo"] = str(input('Sexo [M/F]: ')).upper()
    if pessoa["Sexo"] == 'F':
        mulheres.append(pessoa['Nome'])
    idades.append(pessoa['Idade'])
    pessoas.append(pessoa.copy())
    cadastros += 1
    r = str(input('Quer continuar? [S/N]: ')).strip().upper()
    if r == 'N':
        print('Analisando dados...')
        sleep(1)
        break

media = sum(idades) / len(idades)
idade_acima = [pessoa['Nome'] for pessoa in pessoas if pessoa['Idade'] > media]
print('-='*20)
print(f'- Foram cadastradas {cadastros} pessoas.')
print(f'- A média de idade do grupo é de {media:.1f} anos.')
print(f'- Lista com todas as mulheres: {mulheres}')
print('- Lista das pessoas que estão acima da média:')
print(f'As pessoas com a idade acima da média são:')
for nome in idade_acima:
    print(f'\t{nome}')
