a = int(input('Digite um valor: '))
b = int(input('Digite outro valor: '))
c = int(input('Digite mais um valor: '))
if (a + b>= c) and (a + c >= b) and (b + c >= a):
    print('Esse triangulo é valido, formando um ', end='')
    if a == b == c:
        print('EQUILÁTERO!')
    elif a != b != c != a:
        print('ESCALENO')
    else:
        print('ISÓSCELES')
else:
    print('Esse objeto precisa de ajustes, tente novamente!')