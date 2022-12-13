while True:
    sac = int(input('Quantos RS você quer sacar? '))
    cin = vin = dez = um = 0
    cem = cinco = dois = 0
    val = sac
    if sac >= 100:
        cem = int(sac / 100)
        sac = sac % 100

    elif sac >= 50:
        cin = int(sac / 50)
        sac = sac % 50

    elif sac >= 20:
        vin = int(sac / 20)
        sac -= (vin*20)

    elif sac >= 10:
        dez = int(sac / 10)
        sac -= (dez*10)

    elif sac >= 5:
        cinco = int(sac / 5)
        sac -= (cinco*5)

    elif sac >= 2:
        dois = int(sac / 2)
        sac -= (dois*2)

    elif sac >= 1:
        um = sac
    print('-' * 30)
    print(f'''O valor de {val}
Pode ser sacado em 
{cem} notas de cem reais
{cin} notas de cinquenta reais
{vin} notas de vinte reais
{dez} notas de dez reais
{cinco} notas de cinco reais
{dois} notas de dois reais
{um} moedas de um real''')
    cont = str(input('Quer sacar mais? [S/N]')).strip().upper()[0]
    if cont == 'N':
        break