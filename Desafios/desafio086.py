lista = [[], [], []]
cont = 0
cont1 = -1
for c in range(0, 9):
    num = int(input(f'Digite um valor para {cont, cont1 + 1}: '))
    cont1 += 1
    if cont1 == 3:
        cont += 1
        cont1 = 0
    if cont == 0:
        lista[0].append(num)
    elif cont == 1:
        lista[1].append(num)
    else:
        lista[2].append(num)
print('-=' * 40)
print(f'{lista[0]}\n{lista[1]}\n{lista[2]}')
print('-=' * 40)
