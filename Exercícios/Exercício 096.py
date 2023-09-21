def area():
    print('CONTROLE DE TERRENOS')
    print('-'*20)
    l = float(input('LARGURA (m): '))
    c = float(input('COMPRIMENTO (m): '))
    aream2 = c * l
    print(
        f'A área de um terreno {l:.1f}x{c:.1f} é de {aream2:.1f}m².')


area()
