viagem = float(input('Informe a distancia que será percorrida: '))
'''if viagem <=200:
    preco = viagem * 0.50
else:
    preco = viagem * 0.45'''
preco = viagem * 0.50 if viagem <= 200 else viagem  * 0.45
print(f'O Valor da passagem ficou por R${preco:.2f}')