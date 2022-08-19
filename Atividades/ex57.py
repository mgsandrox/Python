

sex = str(input('Qual o seu sexo:[M/F] ')).strip().upper()[0]
while sex not in 'MF':
    sex = str(input('Dados inválidos. Por favor tente novamente:[M/F] ')).strip().upper()[0]
print(f'Sexo {sex} registrado com sucesso!')