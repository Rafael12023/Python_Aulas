import time
a = float(input('informe a sua velocidade: '))

print('Processando o Sistema\n')
time.sleep(2)
if a > 80:
    print('Velocidade Acima do permitido')
    print('A sua multa vai ser de R${:.2f}'.format((a-80)*7))
else:
    print('Velocidade Permitida')

print('Siga a viagem')

