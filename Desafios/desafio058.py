from random import randint

num = int(input('Digite um número entre 0 e 10: '))
n1 = randint(0, 10)
p = 0

while n1 != num:
    num = int(input('Que pena, você errou. Tente Novamente:'))
    p += 1
print('O número era {}, você acertou, Parabéns! Você precisou de {} palpites'.format(n1, p))