print('aluguel de carros')

dia = int(input('quantos dias eu andei com o carro alugado:\t'))
km = float (input('quantos km eu andei com o carro alugado: \t'))

dia = dia * 60
km = km * 0.15

valortotal = dia + km

print('o valor total a pagar é de R${:.2f}'.format(valortotal))