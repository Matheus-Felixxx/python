from random import randint
from time import sleep
def linha():
    print('-=' * 40)


for c in range(0, 5):
    linha()
    lista = list()
    maior = 0
    limit = randint(0, 6)
    print(f'Analisando os valores passados...')
    sleep(1)
    for _ in range(0, limit):
        rand = randint(0, 9)
        lista.append(rand)
    for v, a in enumerate(lista):
        sleep(1)
        print(a, end=' ')
    print(f' Foram informados {len(lista)} valores ao todo')
    for v, a in enumerate(lista):
        if v == 0:
            maior = a
        else:
            if a > maior:
                maior = a
    print(f'O maior número informado foi {maior}')
    lista.clear()