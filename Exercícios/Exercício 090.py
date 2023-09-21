aluno = {}
aluno['Nome'] = str(input('Nome do aluno: '))
aluno['Média'] = float(input(f'Digite a média de {aluno["Nome"]}: '))
media = aluno['Média']
print(f'Nome: {aluno["Nome"]}')
print(f'Média: {aluno["Média"]}')
if aluno['Média'] >= 7:
    aluno['situação'] = 'aprovado'
elif 4 < aluno['Média'] < 7:
    aluno['situação'] = 'recuperação'
else:
    aluno['situação'] = 'reprovado'
print(aluno['situação'])
