numero = int(input('Insira um numero: '))
if (numero%2):
    print(f'O \033[1;34m{numero}\033[m é ímpar')
else:
    print(f'O \033[1;31m{numero}\033[m é par')