c = float(input('Informe a temperatura em °C: '))
f = c * 1.8 + 32
k = c + 273
c1 = (f - 32) / 1.8
k1 = (((f - 32) * 5) / 9) + 273
f1 = ((k - 273) * 1.8) + 32
c2 = k - 273
print(f' A conversão de {c}°C para fahrenheit e de {f}°F e em kelvin é {k}°K')
print(f'A conversão de {f}°F para celcius {c1}°C  e de kelvin é {k1}°K ')
print(f'A conversão de {k}°K para fahrenheit {f1}°F e  para celsius {c2}°C')