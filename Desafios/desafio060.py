num = int(input('Digite um Valor:'))
num2 = num
r = 1

while num2 != 0:
    r = r * num2
    num2 -= 1
print('O resultado da fatorial é {}'.format(r))
