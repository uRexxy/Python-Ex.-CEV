from time import sleep


def fatorial(n, show=bool):
    """
    -> Calcula o Fatorial de um número.
    :param n: O número a ser calculado.
    :param show: (opcional) Mostrar ou não a conta.
    : return: O valor do Fatorial de um números n.
    """

    print('_'*20)
    if show:
        fato = 1
        num = n
        for num in range(num, 0, -1):
            print(num, end=' ', flush=True)
            sleep(0.2)
            fato *= num
        print('=', end=' ')
        return fato
    else:
        fato = 1
        num = n
        for num in range(num, 0, -1):
            fato *= num
        return fato


help(fatorial)
print(fatorial(5, True))
