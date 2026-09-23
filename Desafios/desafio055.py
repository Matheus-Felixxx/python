peso = float(input('Peso: '))
maior = peso
menor = peso
for c in range(0, 4):
    peso1 = float(input('Peso: '))
    if peso1 > maior:
        maior = peso1
    elif peso1 < menor:
        menor = peso1
print('o menor peso foi {} e o maior {}'.format(menor, maior))