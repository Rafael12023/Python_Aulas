#Verificando se pode criar um triagulo

a = float(input('informe um numero: '))
b = float(input('informe um numero: '))
c = float(input('informe um numero: '))


if a == b == c:
    print('pode formar um triangulo equilatero')

if a < b + c and b < a + c and c < a + b:
    print('pode formar um tringulo')

else:
    print('não pode formar um triangulo')