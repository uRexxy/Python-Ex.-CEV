import random
chute = int(input('Digite um número de 0 a 5: '))
n = random.randint(0, 5)
if chute == n:
    print('Você venceu!')
else:
    print('Você perdeu!')
