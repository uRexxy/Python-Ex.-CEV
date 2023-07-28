import random
t = 1
print('Sou seu computador...\n Estou pensando em um número de 0 a 10.\n Será que tu comsegue advinhar?')
n = random.randint(1, 10)
c = int(input('Qual o seu palpite? '))
while c != n:
    if c > n:
        c = int(input('Menos... Tente mais uma vez: '))
    elif c < n:
        c = int(input('Mais... Tente mais uma vez: '))
    t += 1
print(f'Acertou!\nO número era {n}\nGastastes {t} tentativas. Parabéns!')
