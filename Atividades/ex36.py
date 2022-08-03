imo = float(input('Qual o valor do imovél desejado: R$'))
anos = int(input('Em quantos anos deseja parcelado: '))
sal = float(input('Qual seu salario: R$'))
meses = anos * 12
presta = imo / meses

if presta > sal * 0.3:
    print(f'O financiamento foi negado o valor da paracela é de R${presta:.2f} e o valor atual do seu salario é de \033[1;31m R${sal:.2f}\033[m')
elif presta < sal * 0.3:
    print(f'Financiamento liberado! suas parcelas são de R${presta:.2f} que serão pagas em {meses} meses ou seja dentro de {anos} anos, aproveite o imovél!!!')
