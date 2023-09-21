termo = int(input('Primeiro termo: '))
r = int(input('Razão: '))
decimo = termo + (10 - 1) * r
for i in range(termo, decimo + r, r):
    print(i, end=' → ')
print('ACABOU')
