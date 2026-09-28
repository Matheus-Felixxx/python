r = 1
c = 0
s = 0
ma = 0
me = 0

while r != 0:
    r = int(input('Digite um valor para calcular a média desses valores. O programa irá parar ao ser digitado 0:'))
    if r != 0:
        c += 1
        s += r
        if c == 1:
            ma = r
            me = r
        elif c > 1:
            if r > ma:
                ma = r
            elif r < me:
                me = r

    elif r == 0:
        r = int(input('Quer continuar digitando? ([1] Sim [0] Não): '))
if c > 0:
    m = s / c
    print('A média desses valores é igual a {} o maior valor foi {} e o menor foi {}'.format(m, ma, me))