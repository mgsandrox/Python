total= totmil = menor = cont = 0
barato = ''
while True:
    produto = str(input('Nome do produto: '))
    preço = float(input('Preço: R$'))
    cont += 1
    total += preço
    if preço > 1000:
        totmil += 1
    if cont == 1 or preço < menor:
        menor = preço
        barato = produto
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Deseja continuar: [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
print(f'O total da compra {total:10.2f}')
print(f'A quantidade de produtos com mais de R$1000 foi de {totmil}')
print(f'O produto mais barato foi {barato} custando {menor}')
print('Fim do programa!')