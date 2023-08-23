nome = str(input('Digite seu nome completo: ')).strip()
print('Analisando nome...')
nomemai = nome.upper()
print(f'Seu nome em maiúsculas é {nomemai}')
nomemin = nome.lower()
print(f'Seu nome em minúsculas é {nomemin}')
nomeesp = nome.replace(" ", "")
nomecont = len(nomeesp)
print(f'Seu nome tem ao todo {nomecont} letras')
nomepri = nome[0:6]
nomeprilen = len(nomepri)
print(f'Seu primeiro nome é {nomepri} e ele tem {nomeprilen}')

print('+'*20)

print(f'Seu nome em maiúsculas é {nome.upper()}')
print(f'Seu nome em minúsculas é {nome.lower()}')
print(f'Seu nome tem {len(nome.replace(" ", ""))} letras')
print(f'{nome[0:6]} tem {len(nome[0:6])} letras')
