reais = float(input(('Quanto deseja converter? R$')))
dolar = reais / 5.06
euro = reais / 5.27
bitcoin = reais / 149.51709
print("Sua conversão em dolar foi ${:.2f} \n Sua conversão em euro foi E${:.2f} \n Sua conversão em bitcoin foi B${:.2f} ".format(dolar, euro, bitcoin))
