num = int(input('Digite um numero: '))
mult = 0
for count in range(1, num +1):
    if(num % count == 0):
        print('\033[34m', end=' ')
        mult += 1
    else:
        print('\033[31m', end=' ')
    print(f'{count}', end='')
print(f'\nO número {num} foi divisível {mult} vezes')
if (mult == 2):
    print('É primo!')
else:
    print('Ele não é primo primo')
