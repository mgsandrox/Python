dias = int(input('Quantos dias de alugado? '))
km = float(input('Quantos km rodados? '))
pago = (dias * 60) + (km * 0.15)
print(f'O valor do aluguel por {dias} e por {km}km rodados foi de R${pago:.2f}')