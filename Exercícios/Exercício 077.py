palavras = ('aprender', 'programar', 'linguagem', 'python', 'curso', 'gratis',
            'estudar', 'praticar', 'trabalhar', 'mercado', 'programador', 'futuro')
vogais = []
for p in palavras:
    print(f'\nNa plavra {p.upper()} temos', end=' ')
    for letra in p:
        if letra in 'aeiou':
            print(letra, end=' ')
