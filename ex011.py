print('Programa para calcular quantos litros de tinta será necessário para pintar a parede')

a = float(input('Informe a altura da parede'))
b = float(input('Informe a largura da parede'))

tamanho_parede = a * b
tamanho_parede = tamanho_parede / 2

print('Você irá gastar {:.2f} litros para pintar a parede' .format(tamanho_parede))