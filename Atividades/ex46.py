from time import sleep
from random import randint
print(''' 
[1] Vou acender os fogos!!!
[2] Não vou acender!
''')
cont = int(input('Qual a sua escolha: '))
if cont == 1:
    for c in range(10,-1,-1):
        print(c)
        sleep(1)
    print('BUM BUMM POWW!')
    sleep(1)
    print('Fogos acesos!!')
elif cont == 2:
    sleep(1)
    print('Ficou com medo né!!!')
else:
    print('Opção invalida!!')
