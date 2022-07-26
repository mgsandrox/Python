from datetime import date
print('Qual ano deseja saber se é bisexto, caso deseje saber o ano atual digite 0! ')
ano = int(input('Digite o ano: '))
if ano == 0:
   ano = date.today().year

if ano % 4 == 0 and ano % 100 !=0 or ano % 400 == 0:
    print(f'Esse ano de \033[1;34m{ano}\033[m é bissexto!')

else:
    print(f"Esse ano \033[1;35m{ano}\033[m não é bissexto!" )