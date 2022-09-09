
pri_termo = int(input('Digite o primeiro Termo: '))
razao = int(input('Digite a Razão da PA: '))
termo = pri_termo
cont = 1
while cont <= 10:
       print('{} --> '.format(termo), end='')
       termo += razao
       cont += 1