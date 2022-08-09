soma = 0
cont = 0
for c in range(1, 7):
    n1 = int(input('Digite um número: '))
    if n1 % 2 == 0:
        soma = soma + n1
        cont += 1
    elif n1 % 2 == 1:
        soma += n1
        cont += 1
print(f'Foram informados {cont} números e a soma foi {soma}')

