a = str(input('informe o seu nome: ')).strip()
nome = a.split()
print('o seu primeiro nome é: {}'.format(nome[0]))
print('o Seu ultimo nome é: {}'.format(nome[len(nome)-1]))
