sal = float(input('Qual o valor do salario: '))

if sal <= 1250:
    novo = sal + (sal * 15 / 100)
else:
    novo = sal + (sal * 10 / 100)
print(f'O novo salario é de R$\033[1;34m{novo}\033[m')