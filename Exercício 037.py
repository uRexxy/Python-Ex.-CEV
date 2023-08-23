print('='*35)
n = int(input('Digite um numero inteiro para a conversão: '))
print("""
[ 1 ] para binário;
[ 2 ] para octal; 
[ 3 ] para hexadecimal;
""")
c = int(input('Sua opção: '))

if c == 1:
    binario = bin(n)[2:]
    print(f'O número {n} em binário é {binario}.')
elif c == 2:
    octal = oct(n)[2:]
    print(f'O número {n} em octal é {octal}.')
elif c == 3:
    hexa = hex(n)[2:]
    print(f'O número {n} em hexadecimal é {hexa}.')
else:
    print('Escolha uma das opções para a conversão.')
print('='*35)
