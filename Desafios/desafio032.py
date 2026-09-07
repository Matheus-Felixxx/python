ano = int(input('Digite um ano: '))
bi = ano % 4

if bi == 0 :
    b1 = ano % 100
    if b1 == 0:
        b2 = ano % 400
        if b2 == 0:
            print('{} é um ano bissexto'.format(ano))
        else:
            print('{} não é um ano bissexto'.format(ano))
    else:
        print('{} é um ano bissexto'.format(ano))

else:
    print('{} não é um ano bissexto'.format(ano))