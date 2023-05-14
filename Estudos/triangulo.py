import math
base =  float(input('Informe o valor da base: '))
altura = float(input('Informe o valor da altura: '))

area = base * altura
peri = 2 * (base + altura)
diagonal = math.sqrt(base ** 2 + altura ** 2)

print(f'O valor da área é de {area:.4f}')
print(f'O valor da perimetro é de {peri:.4f}')
print(f'O valor da diagonal é de {diagonal:.4f}')