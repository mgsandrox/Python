prod = float(input('Qual o valor do produto? '))
desc = float(input('Qual o valor do desconto desejado? '))
desconto = desc * prod / 100
promocao = prod - desconto

print(f'O valor do desconto foi de {desconto:.2f} você irá levar o produto por {promocao:.2f}!')
