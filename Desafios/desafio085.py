lista = [[], []]
for c in range(0, 7):
    l1 = int(input(f'Digite o valor {c + 1}°: '))
    if l1 % 2 == 0:
        lista[0].append(l1)
    else:
        lista[1].append(l1)
lista[0].sort()
lista[1].sort()
if len(lista[0]) == 0:
    print(f'Não foi digitado nenhum número par')
else:
    print(f'Os valores pares digitados foram: {lista[0]}')
if len(lista[1]) == 0:
    print(f'Não foi digitado nenhum número ímpar')
else:
    print(f'Os valores ímpares digitados foram: {lista[1]}')