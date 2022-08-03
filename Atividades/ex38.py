n1 = int(input('Insira o primeiro numero: '))
n2 = int(input('Insira o segundo numero: '))

if n1 > n2:
    print(f'O numero {n1} é maior que o numero {n2}')
elif n1 < n2:
    print(f'O numero {n2} é maior que o numero {n1}')
elif n1 == n2:
    print(f'Os numeros {n1} e {n2} são iguais')