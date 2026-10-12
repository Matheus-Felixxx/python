lista = [[], [], [], []]
maior = 0
cont = 0
cont1 = -1
soma = 0

for c in range(0, 9):
    num = int(input('Digite um valor para {}: '.format((cont, cont1 + 1))))
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

    if num % 2 == 0:
        lista[3].append(num)

print('-=' * 40)
print('{}\n{}\n{}'.format(lista[0], lista[1], lista[2]))
print('-=' * 40)

# Soma dos valores pares
for c in lista[3]:
    soma += c

if len(lista[3]) == 0:
    print('Não foi digitado nenhum número par.')
else:
    print('A soma de todos os números pares é {}'.format(soma))

# Soma dos valores da terceira coluna
soma = lista[0][2] + lista[1][2] + lista[2][2]
print('A soma dos valores da terceira coluna é {}'.format(soma))

# Maior valor da segunda linha
maior = lista[1][0]
for c in range(1, 3):
    if lista[1][c] > maior:
        maior = lista[1][c]

print('O maior valor da segunda linha é {}'.format(maior))