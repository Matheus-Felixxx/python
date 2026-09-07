s1 = float(input('Quanto você recebe: '))
if s1 > 1250.00:
    c1 = ((s1 * 10) / 100) + s1
    print('Como seu salário é maior que R$1250.00 você recebeu um aumento de 10%. Seu salário atual é R${:.2f}'.format(c1))
else:
    c2 = ((s1 * 15) / 100) + s1
    print('Como seu salário é menor ou igual a R$1250.00 você recebeu um aumento de 15%. Seu salário atual é R${:.2f}'.format(c2))