import time
n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro valor: '))
usuario = 0
while usuario != 5:
    print('=-='*10)
    print('[1] SOMAR\n[2] MULTIPLICAR\n[3] MAIOR\n[4] NOVOS NÚMEROS\n[5] SAIR DO PROGRAMA')
    usuario = int(input('Sua escolha: '))
    print('=-='*10)
    if usuario == 1:
        print(f'A soma entre {n1} e {n2} é {n1+n2}')
    elif usuario == 2:
        print(f'A multiplicação entre {n1} e {n2} é {n1*n2}')
    elif usuario == 3:
        maior = max(n1, n2)
        print(f'O maior número entre {n1} e {n2} é {maior}')
    elif usuario == 4:
        n1 = int(input('Digite um valor: '))
        n2 = int(input('Digite outro valor: '))
    elif usuario == 5:
        print('Finalizando...')
        time.sleep(2)
    else:
        print('Digite uma opção válida.')
    time.sleep(1)
print('Fim do programa!')
