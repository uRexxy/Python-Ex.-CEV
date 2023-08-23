from datetime import datetime

cont = 0
ano_atual = datetime.now().year
dados = {}
dados['Nome'] = str(input('Nome: ')).strip()
dados['Ano de nascimento'] = int(input('Ano de nascimento: '))
dados['Idade'] = (dados['Ano de nascimento'] - ano_atual) * -1
dados['Carteira de trabalho'] = int(input('Carteira de Trabalho: '))
if dados['Carteira de trabalho'] != 0:
    dados['Ano de contratação'] = int(input('Ano de contratação: '))
    dados['Salário'] = float(input('Salário: '))
    ano_contratado = dados['Ano de contratação']
    anos_trabalhados = (ano_contratado - ano_atual) * -1
    while anos_trabalhados < 35:
        cont += 1
        anos_trabalhados += 1
print(
    f'Nome: {dados["Nome"]}\nIdade: {dados["Idade"]}\nCTPS:{dados["Carteira de trabalho"]}')
print(f'Contratação: {dados["Ano de contratação"]}\nSalário: {dados["Salário"]}' if dados['Carteira de trabalho'] > 0 else print(
    'Não possui carteira de trabalho.'))
print(
    f'Se aposentara em {(anos_trabalhados + ano_contratado)} com {dados["Idade"] + ((dados["Ano de contratação"] + 35)- ano_atual)} anos de idade' if dados['Carteira de trabalho'] > 0 else print())
