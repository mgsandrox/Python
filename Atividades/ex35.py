a = int(input('Digite um valor: '))
b = int(input('Digite outro valor: '))
c = int(input('Digite mais um valor: '))


if (a + b>= c) and (a + c >= b) and (b + c >= a):
    print('Esse triangulo é valido!')
else:
    print('Esse objeto precisa de ajustes, tente novamente')