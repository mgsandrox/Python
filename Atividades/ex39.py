from _datetime import date
nasc = int(input('Qual o ano do seu nascimento: '))
ano = date.today().year
idade = ano - nasc


if idade < 18:
    dife = 18 - idade
    print(f'Ainda não está no momento faltam {dife} anos para você se alistar, sua idade ainda é {idade} anos')
    alista = ano + dife
    print(f'Seu alistamento será em {alista}')
elif idade == 18:
    print(f'Já está no momento de se alistar sua idade é {idade}, vá a uma junta militar mais proxima!')
elif idade > 18:
    dife = idade - 18
    print(f'Já passou {dife} anos do seu alistamento, sua idade atual é de {idade} anos')
    alista = ano - dife
    print(f'Seu alistamento foi em {alista}')
