

print('_'*35)


def voto(nasc=int(input('Em que ano você nasceu? '))):
    from datetime import datetime
    ano_atual = datetime.now().year
    idade = ano_atual - nasc
    if 16 <= idade < 18 or idade >= 65:
        return 'Voto Opcional'
    if idade < 16:
        return 'Voto Negado'
    if idade >= 18:
        return 'Voto Obrigatório'


print(voto())
