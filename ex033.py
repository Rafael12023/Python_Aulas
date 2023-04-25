#Verificando o menor e maior valor
a = input('informe um valor: ')
b = input('informe um valor: ')
c = input('informe um valor: ')

#Verificando o menor valor
menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c

#Verificando o Maior Valor
maior = a

if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c

print('o menor valor é {}'.format(menor))
print('o maior valor é {}'.format(maior))
