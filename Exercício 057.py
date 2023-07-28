sexo = str(input('Qual o seu sexo? [M/F]? ')).upper().strip()
while sexo not in 'MF':
    sexo = str(input('Dados inválidos. Por favor, Informe seu sexo: ')).upper().strip()
print('Validação concluida.')
