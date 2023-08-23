f = str(input('Digite uma frase: ')).strip().upper()
print(f"A letra 'A' apareceu {f.count('A')} vezes na frase.")
print(f"A primeira letra 'A' apareceu na posição {f.index('A') + 1}")
print(f"A última letra 'A' apareceu n posição {f.rindex('A') + 1}")
