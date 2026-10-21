from random import randint
from time import sleep
lista = list()

def sorteia():
    for c in range(0, 5):
        rand = randint(1, 9)
        lista.append(rand)
def soma():
    par = 0
    for v, c in enumerate(lista):
        if lista[v] % 2 == 0:
            par += lista[v]
    print(par)
sorteia()
print(f'Sorteando 5 valores da lista: ', end='')
for c in lista:
    print(c, end=' ')
    sleep(1)
print('PRONTO!!!')
print(f'Somando os valores pares de {lista}, temos: ', end='')
soma()
