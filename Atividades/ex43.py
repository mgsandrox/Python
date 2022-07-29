peso = float(input('Insira o seu peso atual: KG '))
altura = float(input('Informe agora sua altura: '))

massa = peso / (altura * altura)

if massa < 18.5:
    print(f'Você está abaixo do pesso ideal, porfavor se aliemente melhor sua massa atual é de {massa:.3f}')
elif massa >= 18.5 and massa <= 24.9:
    print(f'Sua massa está no ideal, sua massa atual é de {massa:.3f}')
elif massa >= 25.0 and massa <= 29.9:
    print(f'Você está com sobrepeso, porfavor se cuide sua massa atual é de {massa:.3f}')
elif massa >= 30.0 and massa <=39.9:
    print(f'Você está com obesidade busque um médico e um nutricionista, sua massa atual é de {massa:.3f}')
else:
    print(f'Você vai morre, mude seu estilo de vida já seu IMC é de {massa:.3f}')



