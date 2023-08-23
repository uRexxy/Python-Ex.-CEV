from time import sleep


def contador(inicio, fim, passo):
    print('-='*25)
    print('Contagem de 1 até 10 de 1 em 1')
    for n in range(1, 11, 1):
        print(n, end=' ', flush=True)
        sleep(0.3)
    print('Fim')

    print('-='*25)
    print('Contagem de 10 até 0 de 2 em 2')
    for n in range(10, -1, -2):
        print(n, end=' ', flush=True)
        sleep(0.3)
    print('Fim')

    print('-='*25)
    print('Agora é sua vez de personalizar a contagem!')
    inicio_ = int(input('Início: '))
    fim_ = int(input('Fim: '))
    passo_ = int(input('Passo: '))

    def cont_pers(inicio_, fim_, passo_):

        print(f'Contagem de {inicio_} até {fim_} de {passo_} em {passo_}')
        if passo_ == 0:
            passo_ = 1
        elif passo_ < 0:
            passo_ = passo_ * -1

        if passo_:
            if inicio_ > fim_:
                passo_ = passo_ * -1
            elif fim_ > inicio_:
                passo_ = passo_ * 1

        for n in range(inicio_, fim_, passo_):
            print(n, end=' ', flush=True)
            sleep(0.3)
        print('Fim')
    cont_pers(inicio_, fim_, passo_)


contador(0, 0, 0)
