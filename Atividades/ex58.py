from random import randint
pc = randint(0,10)
print('Pensei em um numero entre 0 e 10, qual será?')
acertou = False
chances = 0

while not acertou:
    jogador = int(input('Qual o seu palpite: '))
    chances += 1
    if jogador == pc:
        print('Acertou mizerave!!!')
        acertou = True
    else:
        if jogador > pc:
            print('Um pouco menos, tente de novo')
        elif jogador < pc:
            print('Um pouco mais, tente de novo')

print(f'Fim do jogo, você tentou {chances} vezes até acertar...')