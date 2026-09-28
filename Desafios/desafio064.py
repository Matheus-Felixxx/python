r = 0
c = 0
s = 0

while r != 999:
    r = int(input('Digite um valor de 1 a 999:'))
    c += 1
    if r != 999:
        s += r
print('Você digitou {} números, a soma deles desconsiderando o último é {}'.format(c, s))