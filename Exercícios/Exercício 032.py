from datetime import date
ano = int(input('Diga um ano qualquer. digite 0 para analisar o ano atual! '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f'O ano {ano} é BISSXETO')
else:
    print(f'O ano {ano} não é BISSEXTO')
