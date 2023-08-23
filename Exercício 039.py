from datetime import datetime
nas = int(input('Ano de nascimento: '))
ano = datetime.now().year
idade = ano - nas
print(f'Quem nasceu em {nas} tem {idade} anos em {ano}.')
if idade == 18:
    print('Você deve se alistar IMEDIATAMENTE!')
elif idade > 18:
    nas = nas + 18
    print(f'Seu alistamento foi em {nas}.')
elif idade < 18:
    print('Não está na idade para se alistar.')
