print('-='*20)
print('Analisador de Triângulos')
print('-='*20)
print()
seg1 = float(input('Primeiro segmento: '))
seg2 = float(input('Segundo segmento: '))
seg3 = float(input('Terceiro segmento: '))
if seg1 + seg2 > seg3:
    print('Os segmentos acima podem formar um triângulo.')
else:
    print('Os segmentod acima não podem formar um triângulo.')
