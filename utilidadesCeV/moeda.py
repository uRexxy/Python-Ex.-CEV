def metade(n, mone=False):
    met = n / 2
    if mone:
        met = f'R${n:,.2f}'
        return met
    return met


def dobro(n, mone=False):
    dob = n * 2
    if mone:
        dob = f'R${n:,.2f}'
        return dob
    return dob


def aumentar(n, p, mone=False):
    aumento = n + (n * p / 100)
    if mone:
        aumento = f'R${n:,.2f}'
        return aumento
    return aumento


def diminuir(n, p, mone=False):
    diminucao = n - (n * p / 100)
    if mone:
        diminucao = f'R${n:,.2f}'
        return diminucao
    return diminucao


def monetario(n, mone=False):
    if type(n) == float:
        num = f'R${n:,.2f}'
        return num


def resumo(n, p1, p2):
    if type(n) == float:
        frase = 'RESUMO DO VALOR'
        print('---'*12)
        print(f'{frase:^36}')
        print('---'*12)
        print(f'Preço analisado:   {monetario(n, True):>10}')
        print(f'Dobro do preço:      {monetario(dobro(n), True):>10}')
        print(f'Metade do preço:   {monetario(metade(n), True):>10}')
        print(f'{p1}% do preço:      {monetario(aumentar(n, p1), True):>10}')
        print(f'{p2}% do preço:      {monetario(diminuir(n, p2),True):>10}')
        print('---'*12)
    else:
        print(f'{n}')
