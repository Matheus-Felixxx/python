idade = int(input('A Confederação Nacional de Natação precisa saber sua idade para te cadastrar como atleta e classificar sua categoria. Digite sua Idade:'))
if idade <= 9:
    print('Você foi cadastrado como atleta Mirim')
elif idade <= 14:
    print('Você foi cadastrado como atleta Infantil')
elif idade <= 19:
    print('Você foi cadastrado como atleta Junior')
elif idade <= 20:
    print('Você foi cadastrado como atleta Sênior')
else:
    print('Você foi cadastrado como atleta Master')