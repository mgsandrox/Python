from random import randint
from time import sleep
item = ('Pedra', 'Papel',  'Tesoura' )
pc = randint(0, 2)
print('''
Escolha sua opção:
[0] PEDRA
[1] PAPEL
[2] TESOURA 
''')
jogador = int(input('Qual a sua opção: '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')
sleep(1)
print('-=' * 11)
print(f'O Computador jogou {item[pc]}')
print(f'O jogador jogou {item[jogador]}')
print('-=' * 11)

if pc == 0: # Computador jogou PEDRA
    if jogador == 0:
        print('EMPATE')
    elif jogador == 1:
        print('VITORIA DO JOGADOR')
    elif jogador == 2:
        print('VITORIA DO COMPUTADOR')
    else:
        print('OPÇÃO INVALIDA!')
elif pc == 1: # Computador jogou PAPEL
    if jogador == 0:
        print('VITORIA DO COMPUTADOR')
    elif jogador == 1:
        print('EMPATE')
    elif jogador == 2:
        print('VITORIA DO JOGADOR')
    else:
        print('OPÇÃO INVALIDA!')
elif pc == 2: # Computador jogou TESOURA
    if jogador == 0:
        print('VITORIA DO JOGADOR')
    elif jogador == 1:
        print('VITORIA DO COMPUTADOR')
    elif jogador == 2:
        print('EMPATE')
    else:
        print('OPÇÃO INVALIDA!')
