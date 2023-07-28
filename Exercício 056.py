for i in range(1, 5):
    print('-'*5, f'{i}ᵃ PESSOA', '-'*5)
    if i == 1:
        nome1 = str(input('Nome: '))
        idade1 = int(input('Idade: '))
        sexo1 = str(input('Sexo [M/F]: '))
    elif i == 2:
        nome2 = str(input('Nome: '))
        idade2 = int(input('Idade: '))
        sexo2 = str(input('Sexo [M/F]: '))
    elif i == 3:
        nome3 = str(input('Nome: '))
        idade3 = int(input('Idade: '))
        sexo3 = str(input('Sexo [M/F]: '))
    elif i == 4:
        nome4 = str(input('Nome: '))
        idade4 = int(input('Idade: '))
        sexo4 = str(input('Sexo [M/F]: '))
media = (idade1 + idade2 + idade3 + idade4) / 4
print(f'A média de idsde do grupo é de {media:.1f} anos')
if sexo1 == 'M' or sexo1 == 'm' or sexo2 == 'M' or sexo2 == 'm' or sexo3 == 'M' or sexo3 == 'm' or sexo4 == 'M' or sexo4 == 'm':
    homem = []
    nomes = []
    if sexo1 == 'M' or sexo1 == 'm':
        homem.append(idade1)
        nomes.append(nome1)
    if sexo2 == 'M' or sexo2 == 'm':
        homem.append(idade2)
        nomes.append(nome2)
    if sexo3 == 'M' or sexo3 == 'm':
        homem.append(idade3)
        nomes.append(nome3)
    if sexo4 == 'M' or sexo4 == 'm':
        homem.append(idade4)
        nomes.append(nome4)
    homemvelho = max(homem)
    homens = dict(zip(nomes, homem))
    nome_homem_mais_velho = ''
    idade_homem_mais_velho = homemvelho
    for nome, idade in homens.items():
        if idade == homemvelho:
            nome_homem_mais_velho = nome
            idade_homem_mais_velho = idade
print(
    f'O homem mais velho tem {idade_homem_mais_velho} anos e se chama {nome_homem_mais_velho}.')
if sexo1 == 'F' or sexo1 == 'f' or sexo2 == 'F' or sexo2 == 'f' or sexo3 == 'F' or sexo3 == 'f' or sexo4 == 'F' or sexo4 == 'f':
    mulher = 0
    mulher20 = 0
    idade_mulher = []
    if sexo1 == 'F' or sexo1 == 'f':
        mulher += 1
        idade_mulher.append(idade1)
    if sexo2 == 'F' or sexo2 == 'f':
        mulher += 1
        idade_mulher.append(idade2)
    if sexo3 == 'F' or sexo3 == 'f':
        mulher += 1
        idade_mulher.append(idade3)
    if sexo4 == 'F' or sexo4 == 'f':
        mulher += 1
        idade_mulher.append(idade4)
    for m in idade_mulher:
        if m < 20:
            mulher20 += 1
print(f'Ao todo são {mulher20} mulheres com menos de 20 anos')
