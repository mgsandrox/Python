num = cont = soma = 0
num = int(input('Digite um numero [diferente de 999]: '))
while num != 999:
    soma += num
    cont += 1
    num = int(input('Digite um numero [diferente de 999]: '))
print(f'Você digitou {cont} numeros e a soma deles é {soma}')