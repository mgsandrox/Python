from time import sleep
soma = 0
cont = 0
print('Informe alguns números eles serão somado!!!')
sleep(1)
for c in range(1, 7):
    n1 = int(input('Digite um número: '))
    if n1 % 2 == 0:
        soma = soma + n1
        cont += 1
    elif n1 % 2 != 0:
        soma += n1
        cont += 1
print(f'Foram informados {cont} números e a soma foi {soma}')

