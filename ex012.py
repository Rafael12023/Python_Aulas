
a = float(input('qual o preço do produto'))

desconto = a*5/100
desconto = a - desconto

print('o preço do produto sem desconto é de {:.0f} e com 5% de desconto é de {:.0f}' .format(a, desconto))