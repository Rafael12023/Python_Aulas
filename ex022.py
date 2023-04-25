a = str(input('informe um nome: ')).strip()

#Passando para maiusculo
print('O Seu nome em Maiusculo é {}'.format(a.upper()))
#Passando para minusculo
print(a.lower())
#Contando quantas letras tem na frase. E Quando utilizo Variavel.count(' '), e dentro coloco um espaço, conto sem ele.
print(len(a) - a.count(' '))
#Aparecendo apenas a primeira palavra dos blocos do comando split e usando o len para contar quantas letras tem no nome
separa = a.split()
print('{}, {}'.format(separa[0], len(separa [0])))