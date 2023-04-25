#Verificar se o ano é bissexto
a = int(input('informe um ano para saber se ele é bissexto: '))

b = 'é bissexto'
c = 'não é bissexto'

if a % 4 == 0 and a % 100 != 0 or a % 400 == 0:
    print(b.upper())
else:
    print(c.upper())