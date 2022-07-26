v1 = int(input('Informe o primeiro valor: '))
v2 = int(input('Informe o segundo valor: '))
v3 = int(input('Informe o terceiro valor: '))

lista = [v1,v2,v3]

print(f'O maior valor é de \033[1;31m{max(lista)}\033[m')
print(f'O menor valor é de \033[1;34m{min(lista)}\033[m')