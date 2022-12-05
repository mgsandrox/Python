from time import sleep
c = 1
print('Infome um numero e veja a tabuada e caso queira sair digite 0 ou um numero negativo')
sleep(0.5)
while True:
    num = int(input('Deseja ver qual tabuada: '))
    if num <= 0:
        break
    for c in range (1, 11):
        print(f'{num} X {c} = {num * c}')
    sleep(0.5)
print('Fim da tabuada!')



# Tabuada usando o While
'''
numero = int(input('Quer ver a tabuada de qual número? '))
cont = 0
total = 0
while numero >= 0 :
    while cont <= 10:
        total += 1
        resultado = numero * cont
        print(numero, 'x', cont, '=', resultado)
        cont += 1
    cont = 0
    numero = int(input('Quer ver a tabuada de qual número? '))
'''