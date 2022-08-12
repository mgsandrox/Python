# Minha maneira de fazer o desafio
list = []
for p in range(1,6):
    peso = float(input(f'Informe o peso da {p}° pessoa: '))
    list += [peso]
print(f'O maior peso é de {max(list)}KG')
print(f'O menor peso é de {min(list)}KG')

#Maneira que o professor fez
'''maior = 0
menor = 0
for p in range(1,6):
    peso = float(input(f'Informe o peso da {p}° pessoa: '))
    if p == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        elif peso < menor:
            menor = peso
print(f'O maior peso é {maior}Kg')
print(f'O menor peso é {menor}Kg')'''



