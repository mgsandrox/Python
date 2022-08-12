somaidade = 0
media = 0
maiorhomem = 0
nomevelho = ''
totmulher = 0
for p in range(1, 5):
    print(f'-----------{p}° PESSOA ----------')
    nome = str(input("Informe o nome: ")).strip()
    idade = int(input('Informe a idade: '))
    sexo = str(input('Informe o sexo [M/F]: ')).strip()
    somaidade += idade
    if p == 1 and sexo in 'Mm':
        maiorhomem = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > maiorhomem:
        maiorhomem = idade
        nomevelho = nome
    if sexo in 'Ff' and idade <= 20:
        totmulher += 1
media = somaidade / 4
print(f'A mádia de idade é {media} anos')
print(f'O homem mais velho tem{maiorhomem} anos e o nome é {nomevelho}')
print(f'Ao todo são {totmulher} com menos ou 20 anos')