print('-='*5, 'Cadastro de pessoas', '-='*5)
idade = maior_idade = mulheres_vinte = homens = 0
p = 'S'
sexo = ''
while p == 'S':
    sexo = str(input('Qual o sexo [M/F] ')).upper().strip()
    idade = int(input('Qual a idade? '))
    if idade >= 18:
        maior_idade += 1
    if sexo == 'M':
        homens += 1
    if sexo == 'F' and idade <= 20:
        mulheres_vinte += 1
    p = str(input('Quer continuar? [S/N] ')).upper().strip()
    if p == 'N':
        break
print('-='*5, 'FIM DO PROGRAMA', '-='*5)
print(f'Existem {maior_idade} pessoas com mais de 18\n{homens} homens foram cadastrados\n{mulheres_vinte} mulheres com menos de 20 anos')
