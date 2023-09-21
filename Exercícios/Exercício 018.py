from math import radians, sin, cos, tan
angulo = float(input('Digite o valor do ângulo: '))
se = sin(radians(angulo))
print(f'O ângulo de {angulo} tem o SENO de {se:.2f}')
co = cos(radians(angulo))
print(f'O ângulo de {angulo} tem o COSSENO de {co:.2f}')
tan = tan(radians(angulo))
print(f'O ângulo de {angulo} tem a TANGENTE de {tan:.2f}')