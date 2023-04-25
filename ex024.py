#Verificando se o nome vai ser sempre Santo com booleano, sendo que o usuario digite da forma que quiser 'Santo" e transformando em maisuculo

a = input('informe a sua cidade: ').strip()
print(a[:5].upper() == "SANTO")