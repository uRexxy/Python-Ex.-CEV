from random import randint
n1 = randint(1, 10)
n2 = randint(1, 10)
n3 = randint(1, 10)
n4 = randint(1, 10)
n5 = randint(1, 10)
num = (n1, n2, n3, n4, n5)
num_maior = max(num)
num_menor = min(num)
print(
    f'Os números aletórios são: {num}\nO menor número é {num_menor}\nO maior número é {num_maior}')
