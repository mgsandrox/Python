from time import sleep
n1 = int(input('Insira o primeiro valor: '))
n2 = int(input('Insira o segundo valor: '))
opção = 0
lista = [n1, n2]

while opção != 5:
    print('''Menu:
    [ 1 ]Soma
    [ 2 ]Multiplicar
    [ 3 ]Maior
    [ 4 ]Novo número
    [ 5 ]Sair do programa
    ''')
    opção = int(input('Qual sua opção:'))

    if opção == 1:
        resul = n1 + n2
        print(f'A soma de {n1} + {n2} o resultado é de  {resul}')

    elif opção == 2:
        resul = n1 * n2
        print(f'A multiplicação de {n1} e {n2} da o resultado de {resul}')

    elif opção == 3:
        print(f'O maior valor entre {n1} e {n2} é o valor {max(lista)}')

    elif opção == 4:
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor:'))

    elif opção == 5:
        print('Finalizando...')

    else:
        print('>>>>>>>> Opção Inválida! <<<<<<<<<')
    print('=*=' * 10)
    sleep(2)
print('>>>>>>>>>>Fim do Programa!<<<<<<<<<<<')