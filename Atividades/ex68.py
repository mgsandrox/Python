from random import randint
v = 0
while True:
    jogador = int(input('Digite um valor: '))
    computador = randint(0, 10)
    total = jogador + computador
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('Par ou Impar? [P/I] ')).strip().upper()[0]
    print(f'Você jogou {jogador} e o computador {computador}. Total de {total}', end= '')
    print(f' Deu par ' if total % 2 == 0 else ' Deu impar')

    if tipo == 'P':
        if total % 2 == 0:
            print('Você venceu!')
            v += 1
        else:
            print('Você Perdeu!')
            break
    elif tipo == 'I':
        if total % 2 == 1:
            print('Você ganhou!')
            v += 1
        else:
            print('Perdeu!')
            break
    print('Vamos tentar outra vez!')
print(f'Game Over!')


