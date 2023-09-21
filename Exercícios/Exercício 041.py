from datetime import date
nasc = int(input('Ano de nascimento: '))
ano = date.today().year
idade = nasc - ano
idade = idade * -1
print(f'O atleta tem {idade} anos.')
if idade <= 9:
    print('Categoria do atleta: MIRIM')
elif idade <= 14:
    print('Categoria do atleta: INFANTIL')
elif idade <= 19:
    print('Categoria do atleta: JÚNIOR')
elif idade <= 25:
    print('Categoria do atleta: SÊNIOR')
elif idade > 25:
    print('Categoria do atleta: MASTER')
