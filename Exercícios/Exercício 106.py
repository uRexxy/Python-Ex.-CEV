from time import sleep


while True:
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    print('  SISTEMA DE AJUDA PyHELP')
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    resp = str(input('Função ou Biblioteca > ')).strip().lower()
    func = f'{resp}'
    if resp == 'fim':
        sleep(0.5)
        break
    sleep(0.5)
    print(f'Acessando o manual do comando {func}...')
    sleep(0.5)
    print()
    print()
    help(f'{func}')
    sleep(0.5)
print('ATÉ LOGO!')
