
#Fatorial do jeito simples
'''from math import factorial
n = int(input('Digitr um numero:'))
f = factorial(n)
print(f'O fatorial de {n} e {f}')'''


#Fatorial mais complicado
n =  int(input('Informe um numero:'))
c = n
f = 1
print(f'Calculando {n}! = ', end='')
while c > 0:
    print(f'{c}', end='')
    print(f' x ' if c > 1 else ' = ', end='')
    f *= c
    c -= 1
print(f'{f}')