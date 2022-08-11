'''frase = str(input('Digite uma palavra: ')).upper().strip()
palavra = frase.split()
junto = ''.join(palavra)
inverso = ''
for letra in range(len(junto) -1, -1, -1):
    inverso += junto[letra]
print(f'O inver do {junto} e {inverso}')
if inverso == junto:
    print("É um palindromo")
else:
    print('Não é um palindromo')'''

#Modo de fazer o palindromo  do python
frase = str(input('Digite uma palavra: ')).upper().strip()
palavra = frase.split()
junto = ''.join(palavra)
inverso = junto[::-1]
print(f'O inver do {junto} e {inverso}')
if inverso == junto:
    print("É um palindromo")
else:
    print('Não é um palindromo')