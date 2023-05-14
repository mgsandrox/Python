cout = 0
soma_idade = 0
while True:
    nome = str(input('Qual o seu nome: ')).upper().strip()
    if nome == 'N':
        break
    idade = int(input('Informe sua idade: '))
    soma_idade += idade
    cout += 1
    media = soma_idade / cout
print(f'O valor da médio das idades citadas informadas é de {media}')
