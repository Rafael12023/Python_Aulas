#Calculando Seno, Cosseno e Tangente
import math
angulo = float(input('informe o angulo que deseja calcular: '))
seno = math.sin(math.radians(angulo))
cosseno = math.cos(math.radians(angulo))
tangente = math.tan(math.radians(angulo))
print('Seno é {:.2f} \nCosseno é {:.2f} \nTangente é {:.2f}'.format(seno, cosseno, tangente))