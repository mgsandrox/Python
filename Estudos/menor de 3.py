menor = 0

p = int(input('Informe um valor: '))
s = int(input('Informe um valor: '))
t = int(input('Informe um valor: '))

if p < s and p < t :
    menor = p
elif s < p and s < t:
    menor = s
else:
    menor = t
print(f'O menor valor entre os informados é {menor}')