sal = float(input('informe o seu salario: R$ '))

if sal <= 1250:
    aumento = sal *15 / 100
    print('o seu salario de R${:.2f} passa a ser de R${:.2f} com 15% de aumento'.format(sal, aumento + sal))
elif sal > 1250:
    aumento = sal *10 /100
    print('o seu salario de R${:.2f} passa a ser de R${:.2f} com 10% de aumento'.format(sal, aumento + sal))

print('PARABENS PELA SUA CONTRIBUIÇÃO NA EMPRESA!!!')