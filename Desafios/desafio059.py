r = 0
while r != 5:
    n1 = int(input('Digite um valor:'))
    n2 = int(input('Digite outro valor:'))
    r = int(input('O que você quer fazer com esses valores: ([1] Somar [2] Multiplicar [3] Maior [4] Novos Números [5] Sair do Programa) '))

    if r == 1:
        n3 = n1 + n2
        print('A soma dos dois valores é igual a {}'.format(n3))
    elif r == 2:
        n3 = n1 * n2
        print('Multiplicando esses dois números o resultado é {}'.format(n3))
    elif r == 3:
        if n1 > n2:
            print('O maior número é {}'.format(n1))
        else:
            print('O maior número é {}'.format(n2))
    elif r == 5:
        print('Programa finalizado')