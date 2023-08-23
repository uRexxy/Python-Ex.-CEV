parede_altura = float(input('Qual a altura da sua parede? [em metros] '))
parede_largura = float(input('Qual a largura da sua parede? [em metros] '))
area = parede_largura * parede_altura
print(
    f'Sua parede tem a dimensão de {parede_largura}x{parede_altura} e sua área é de {area}m².')
tinta = area / 2
print(f'Para pintar essa parede, você precisará de {tinta}L de tinta.')
