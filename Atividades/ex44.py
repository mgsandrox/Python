preco = float(input('Qual o valor das compras? R$'))
print('''
Qual a sua forma de pagamento:
[1] à vista dinheiro/pix
[2] à vista cartão
[3] 2x no cartão
[4] 3x ou mais no cartão
''')
opcao = int(input('Qual é a sua opção? '))

if opcao == 1:
    total = preco - (preco * 10 / 100)
    desconto = (preco * 10) / 100
    print(f'Sua compra de R${preco:.2f} saiu por R${total:.2f} seu desconto foi de R${desconto:.2f}!')
elif opcao == 2:
    total = preco - (preco * 5 / 100)
    desconto = (preco * 5) / 100
    print(f'Sua compra de R${preco:.2f} saiu por R${total:.2f} seu desconto foi de R${desconto:.2f}!')
elif opcao == 3:
    total = preco
    parcela = total / 2
    print(f'Sua parcerla será de 2x de R${parcela}')
    print(f'Sua compra de R${preco:.2f} saiu por R${total:.2f}!')
elif opcao == 4:
    total = preco + (preco * 20 / 100)
    juros = (preco * 20) / 100
    totalpar = int(input('Deseja dividir em 3 ou mais vezes, quantas parcelas serão? '))
    parcela = total / totalpar
    print(f'A compra de R${preco} parcelada de {totalpar} saira por R${total} \n Com parcelas de R${parcela} o acrescimo de  juros de foi R${juros}')
else:
    print('Opção invalida, tente novamente!')