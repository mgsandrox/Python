num = int(input('Qual o numero deseja converter: '))
print('''Escolha uma das base: 
[1] Binario
[2] Octal
[3] Hexadecimal
''')
opcao = int(input('Sua opção: '))

if opcao == 1:
    print(f'O numero digitado em binario é {bin(num)[2:]}')
elif opcao == 2:
    print(f'O numero {num} em octal é {oct(num)[2:]}')
elif opcao == 3:
    print(f'O numero {num} convertido em hexadecimal é {hex(num)[2:]}')
else:
    print('Opção invalida!')