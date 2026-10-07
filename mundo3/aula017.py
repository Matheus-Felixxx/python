# num = list(range(0, 10))
# num[4] = 99
# num.append(300)
# num.sort(reverse=True)
# num.pop()
# num.insert(2, 2)
# num.remove(2)
# print(num)
# print(f'Está lista tem {len(num)} elementos')

valor = []
for cont in range(0, 5):
    valor.append(int(input('digite um valor: ')))
# valor.append(5)
# valor.append(9)
# valor.append(4)

for c, v in enumerate(valor):
    print(f'Na posição {c} tem o número {v}')
print('Cheguei ao final da lista.')