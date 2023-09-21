n = 0
while True:
    n = int(input('Quer ver a tabuada de qual valor? '))
    print('-'*35)
    for i in range(1, 11):
        m = n * i
        print(f'{n} X {i} = {m}')
    print('-'*35)
    if n == 0:
        break
print('PROGRAMA TABUADA ENCERRADO. Volte sempre!')
