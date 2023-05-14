print('Informe 2 numero iguais para finalizar o programa')
while True:
    x = int(input('Informe o valor de X: '))
    y = int(input('Informe o valor de Y: '))
    if x > y:
        decrecente = x > y
        print(f'Os valores de X foi {x} e de {y} por isso são decrescente')
        print('Digite mais 2 numeros')
    elif x < y:
        crescente = x < y
        print(f'Os valores de X foi {x} e de {y} por isso são crescente')
        print('Digite mais 2 numeros')
    else:
        break
        print('Operação finalizada!')