from _datetime import date
ani = int(input('Informe o ano de nascimento: '))
atual = date.today().year
idade = atual - ani

if idade <= 9:
    print(f'Com a idade de {idade} ano(s) você se encontra na categoria MIRIM')
elif idade >=10 and idade <= 14:
    print(f'Com a idade de {idade} ano(s) você se encontra na categoria INFANTIL')
elif idade >=15 and idade <=19:
    print(f'Com a idade de {idade} ano(s) você se encontra na categoria JUNIOR')
elif idade >=20 and idade <=25:
    print(f'Com a idade de {idade} ano(s) você se encontra na categoria SÊNIOR')
else:
    print(f'Com a idade de {idade} ano(s) você se encontra na categoria MASTER')