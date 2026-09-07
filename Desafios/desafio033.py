n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
n3 = int(input('Digite outro número: '))
if n1 < n2:
    if n1 < n3:
        menor = n1
    else:
        menor = n3
else:
    if n2 < n3:
        menor = n2
    else:
        menor = n3
print('o menor número é {}'.format(menor))
if n1 > n2:
    if n1 > n3:
        maior = n1
    else:
        maior = n3
else:
    if n2 > n3:
        maior = n2
    else:
        maior = n3
print('O maior número é {}'.format(maior))