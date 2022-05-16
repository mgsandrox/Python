salario = float(input('Insira o valor do salario atual: R$'))
reajuste = float(input('Insira o valor do reajuste: '))
#valor = salario * reajuste / 100
#novo = salario + valor
novosal = salario + (salario * reajuste / 100)

print(f'Devido a alta da inflação o salario de R${salario:.2f} passarar por um reajuste de {reajuste}% e começara a ser de R${novosal:.2f}')
#print(f'Com a nova atuaização de valores o salario de R${salario:.2f} passarar a ser de {novo:.2f}')
#print(f'O Reajuste foi de {valor:.2f} ')
