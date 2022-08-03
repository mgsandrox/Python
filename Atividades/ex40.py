n1 = float(input('Qual foi a sua primeira nota: '))
n2 = float(input('Qual foi a sua segunda nota:'))
n3 = float(input('Qual foi a sua terceiro nota:'))
media = (n1 + n2 + n3) / 3
if media < 5.0:
    print(f'Você foi \033[1;31mREPROVADO\033[m ,sua média é {media:.1f}')
elif media > 7.0:
    print(f'Voce foi \033[1;34mAPROVADO\033[m, sua media é {media:.1f}')
else:
    print(f'Você está de \033[1;32mRECUPERAÇÃO\033[m, sua média é {media:.1f}')