from time import sleep


def maior(*args):
    print('-='*20)
    print('Analisando valores passados...')
    sleep(0.2)

    for n in args:
        print(n, end=' ', flush=True)
        sleep(0.3)
    print(f'Foram passados {len(args)} valores ao todo.')

    if not args:
        print('Não existe um maior valor.')
    else:
        print(f'O maior valor informado foi {max(args)}.')


maior(2, 70, 23, 1)

maior()

maior(1, 2, 3)

maior(10, 20, 30, 40)

maior(6)
