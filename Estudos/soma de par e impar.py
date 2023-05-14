print('Digite dois numeros')
x = int(input())
y = int(input())

if x > y:
    troca = x
    x = y
    y = troca

soma = 0
for i in range(x+1, y):
    if i % 2 != 0:
        soma += i
print(f' SOMA DOS IMPARES = {soma}')

''''
SUGESTÃO DO CODIGO MAIS LIMPO 

def soma_impares(x, y):
    numeros_impares = [i for i in range(x+1, y) if i % 2 != 0]
    return sum(numeros_impares)

x = input('Digite o primeiro número: ')
y = input('Digite o segundo número: ')

if x.isdigit() and y.isdigit():
    x = int(x)
    y = int(y)

    if x > y:
        x, y = y, x

    soma = soma_impares(x, y)
    print(f'SOMA DOS ÍMPARES = {soma}')
else:
    print('Digite apenas números inteiros')
'''