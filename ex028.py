import random
import time

adversario = random.randint (0, 5) #Sorteio que o computador vai fazer entre 0 a 5.
jogador = int(input('Informe um numero entre 0 a 5: ')) #Numero que o usuário vai informar.
print('PROCESSANDO')
time.sleep(3)
if adversario == jogador:
    print('Você ganhou')
else:
    print('Você Perdeu')
