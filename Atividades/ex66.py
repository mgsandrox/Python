cout = soma = 0
while True:
    num = int(input('Informe um numero ou insira 999 pra parar: '))
    if num == 999:
        break
    cout += 1
    soma += num
print(f'Foram informados {cout} numeros com o valor somado de {soma} ')
