produto = float(input('Qual o preço do produto? R$'))
desconto = produto - (produto * 5 / 100)
print(
    f'Com um desconto de 5%, o produto que custa {produto} agora custará R${desconto:.2f}')
