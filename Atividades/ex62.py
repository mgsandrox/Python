pri_termo = int(input('Digite o primeiro Termo: '))
razao = int(input('Digite a Razão da PA: '))
termo = pri_termo
cont = 1
total = 0
mais = 10
while mais != 0:
       total += mais
       while cont <= total:
              print('{} --> '.format(termo), end='')
              termo += razao
              cont += 1

       print('PAUSA')
       mais = int(input('Qauntos Termos você quer mostrar a mais? '))