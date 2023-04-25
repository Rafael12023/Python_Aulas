#Calculando Hipotenusa, pelo cateto oposto e cateto adjacente
import math
co = float(input('qual o seu cateto oposto'))
ca = float(input('qual o seu cateto adjacente'))
print('O Comprimento da sua hipotenusa é de {:.2f}'.format(math.hypot(co, ca)))

