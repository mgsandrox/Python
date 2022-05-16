prod = float(input('Qual o valor do produto? '))
desc = float(input('Qual o valor do desconto desejado? '))
desconto = desc * prod / 100
promocao = prod - desconto
parcelado = prod + (prod * desc / 100)
print(f'O valor do desconto foi de {desconto:.2f} você irá levar o produto a vista por {promocao:.2f} e se parcelar sairar por {parcelado}')
