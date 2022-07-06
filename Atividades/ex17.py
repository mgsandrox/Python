'''b = float(input('digite o valor do catero adjacente:  '))
c = float(input('Digite o valor do cateto oposto: '))
a = (b **2 + c **2) ** (1/2)

print(f' O Valor da hipotenusa é de {a:.2f}')'''

from math import hypot
co = float(input('Digite o cateto oposto: '))
ca = float(input('Digite o cateto adjacente: '))
hipo = hypot(co, ca)

print(f'O valor da hipotenusa é de {hipo:.2f}')