#sorteando um nome qualquer
import random
nome1 = input('informe um nome: ')
nome2 = input('informe outro nome: ')
nome3 = input('informe outro nome: ')
nome4 = input('informe outro nome: ')
sortear = [nome1, nome2, nome3,nome4]

print('o nome escolhido foi: {}'.format(random.choice(sortear)))