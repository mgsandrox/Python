n = int(input('Quantos numeros voce vai digitar? '))
vet: [float] = [0 for x in range(n)]

i: int
for i in range(0,n):
    vet[i] = float(input('Digite um numero: '))

print()
print('Numeros digitado:')
for i in range(0, n):
    print(f'{vet[i]}:.1f')