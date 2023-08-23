def leiaDin(msg):
    valido = False
    while not valido:
        entrada = str(input(msg)).replace(',', '.')
        if entrada.isalpha() or entrada.strip() == '':
            print(f'ERRO: \"{entrada}\" é um preço inválido.')
        else:
            valido = True
            return float(entrada)


def leiaint(msg=0):

    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('ERRO: Número digitado não é inteiro!')
        except KeyboardInterrupt:
            print('ERRO: Usuário encerrou o programa!')
            return 0 
        else:
            return n


def leiareal(msg=0):

    while True:
        try:
            n = float(input(msg))
        except (ValueError, TypeError):
            print('ERRO: Número digitado não é real!')
        except KeyboardInterrupt:
            print('ERRO: Usuário encerrou o programa!')
            return 0
        else:
            return n
