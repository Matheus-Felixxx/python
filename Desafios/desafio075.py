from os.path import split

lista = []
for c in range(4):
    valor = int(input(f'Digite o {c+1}° valor: '))
    lista.append(valor)
t = tuple(lista)
print(f'Você digitou os valores {t}')
n = t.count(9)
t = t.count(3)
if n == 0:
    print('O valor 9 não foi digitado em nenhuma posição')
else:
    print(f'O valor 9 foi digitado {n} vezes')
if t == 0:
    print('O valor 3 não foi digitado em nenhuma posição')
else:
    print(f'O valor 3 foi digitado {t} vezes')
par = []
for valor in lista:
    if valor % 2 == 0:
        par.append(valor)
print(f'Os valores pares encontrados foram {par}')