soma = 0
cont = 0
for c in range(1,501,2):
   if c % 3 == 0:
        cont += 1 #cont e soma estão representando a mesma coisa
        soma = soma + c
print(f'A soma dos {cont} numeros ímpares são de {soma}')
