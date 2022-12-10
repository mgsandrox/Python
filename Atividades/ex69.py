maior = 0
cout = 0
totf = 0
totm = 0
while True:
    print('Cadastre uma pessoa!')
    idade = int(input('Informe a idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Informe o sexo: [M/F] ')).strip().upper()[0]
    if idade >= 18:
        maior += 1
    elif sexo == 'M':
        totm += 1
    elif sexo == 'F':
        if idade <= 20:
            totf += 1
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Deseja continuar: [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
print(f'O numero de pessoas com mais de 18 anos são {maior}')
print(f'O numero de homens cadastrados foi {totm}')
print(f'O mulheres com menos de 20 anos é de {totf}')
print('Fim do programa!')
