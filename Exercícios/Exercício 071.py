# saque = int(input('Valor total: R$'))
# banco = um = dez = vinte = cinquenta = 0
# while True:
#     if saque >= 50:
#         cinquenta += 1
#         banco += 50
#         if saque >= 20:
#             vinte += 1
#             banco += 20
#             if saque >= 10:
#                 dez += 1
#                 banco += 10
#             else:
#                 um += 1
#                 banco += 1
#     if banco == saque:
#         break
# print(f'Voce precisou de {um} notas de um real\n{dez} notas de dez\n{vinte} notas de vinte\n{cinquenta} notas de cinquenta')
valor = int(input('Valor do saque: R$'))
ced = 50
total = valor
totced = 0
while True:
    if total >= ced:
        total -= ced
        totced += 1
    else:
        if totced > 0:
            print(f'Total de {totced} cédulas de R${ced}')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        totced = 0
        if total == 0:
            break
print('Volte sempre')
