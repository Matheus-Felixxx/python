from datetime import date
nas = int(input('Quando você nasceu? '))
data = date.today()
ano = data.year
idade = ano - nas
if idade < 18:
    temp =  18 - idade
    print('Você ainda vai precisar fazer o alistamento militar, faltam {} anos'.format(temp))
elif idade == 18:
    print('Já está na hora de se alistar!')
elif idade > 18:
    temp = idade - 18
    print('Já passou do tempo de alistamento, já passou {} anos'.format(temp))