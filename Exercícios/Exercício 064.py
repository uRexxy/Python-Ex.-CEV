n = int(input('Digite um número [999 para parar]: '))
cont = soma = 0
while n != 999:
    cont += 1
    soma += n
    n = int(input('Digite um número [999 para parar]: '))
print(f'Tu digitou {cont} números e a soma entre eles é de: {soma}')
