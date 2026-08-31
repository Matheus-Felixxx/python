import random
no1 = str(input('Primeiro Aluno:'))
no2 = str(input('Segundo Aluno:'))
no3 = str(input('Terceiro Aluno'))
no4 = str(input('Quarto Aluno:'))
lista = [no1, no2, no3, no4]
esc = random.choice(lista)
print('O Aluno escolhido foi {}'.format(esc))