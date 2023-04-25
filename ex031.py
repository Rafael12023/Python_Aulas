a = float(input('Qual a distancia da viagem: '))

if a <= 200:
    print('O Valor da viagem de {:.0f}km foi de R${:.2f}'.format(a, a*0.50))
else:
    print('o valor da viagem de {:.0f}km foi de R${:.2f}'.format(a, a*0.45))
