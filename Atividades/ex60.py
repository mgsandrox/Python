#Fatorial do jeito simples
'''from math import factorial
n = int(input('Digitr um numero:'))
f = factorial(n)
print(f'O fatorial de {n} e {f}')'''


#Fatorial mais complicadon =  int(input('Informe um numero:'))
c = n
f = 1
print(f'Calculando {n}! = ', end='')
while c > 0:
    print(f'{c}', end='')
    print(f' x ' if c > 1 else ' = ', end='')
    f *= c
    c -= 1
print(f'{f}')

'''#Fatorial com FOR
numero = int(input("Fatorial de: ") )

resultado=1
for n in range(1,numero+1):
    resultado *= n
'''
print(resultado)