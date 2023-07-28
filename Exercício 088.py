from time import sleep
nomes = ['Maria', 'Júlia', 'Tanielli', 'Guilherme', 'Rafael']
count = 0
for nome in nomes:
    print(f'O nome {nome} está na posição {count} da lista...')
    sleep(1)
    count += 1