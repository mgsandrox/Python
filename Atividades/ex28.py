from random import choice
print('Em qual valor estou pensando de 0 a 10???')
n1 = int(input('Insira um valor: '))
m = choice([0,1,2,3,4,5,6,7,8,9,10])
if n1 == m:
    print(f'Você acertou o numero é {m}!')
else:
    print(f'Acho que você precisa de uma bola de cristal o numero era {m}')