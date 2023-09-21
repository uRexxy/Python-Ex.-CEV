import datetime
ano_atual = datetime.datetime.now().year
maior_idade = 0
menor_idade = 0
saldo = 0
for p in range(1, 8):
    idades = int(input(f'Digite o ano de nascimento da {p}ᵅ pessoa: '))
    saldo = idades + 18
    if saldo <= ano_atual:
        maior_idade += 1
    elif saldo > ano_atual:
        menor_idade += 1
print(f'Das sete pessoas, {maior_idade} são maiores de idade e {menor_idade} são menores de idade.')
