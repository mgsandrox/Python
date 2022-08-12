from datetime import date
atual = date.today().year
maior = 0
menor = 0
for p in range(1, 8):
    nasc = int(input(f'Informe o ano da {p}° nasceu: '))
    idade = atual - nasc
    if idade >= 18:
        maior += 1
    else:
        menor += 1
print(f'Tiveram \033[1;34m{maior}\033[m pessoas maior de idade! \nTiveram \033[1;31m{menor}\033[m pessoas menor de idade!')