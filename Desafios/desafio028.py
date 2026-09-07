from random import randint

num = int(input('Digite um número entre 0 e 5: '))
n1 = randint(0, 5)
if num == n1:
    print('PARABENS!!! VOCÊ ACERTOU O NÚMERO!!!')
else:
    print('Que pena, você errou o número, tente novamente')