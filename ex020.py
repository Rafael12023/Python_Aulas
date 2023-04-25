#sorteado um nome e aparecendo em ordem
import random
nome1 = input('informe o primeiro nome')
nome2 = input('informe o segundo nome')
lista = [nome1, nome2]
random.shuffle(lista)
print(' a lista foi {}'.format(lista))
