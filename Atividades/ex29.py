velocidade = float(input('Qual a velocidade do veiculo? '))
if velocidade > 80:
    print(f'Prepare o seu bolso, você foi MULTADO sua velocidade foi de {velocidade}')
    multa = (velocidade-80) * 7
    print(f'Você deve pagar uma multa de \033[31m R${multa}\033[m sua velocidade foi de\033[35m{velocidade}Km/h\033[m')
print('\033[1;34mTenha um bom dia e se beber não dirija!!!\033[m')