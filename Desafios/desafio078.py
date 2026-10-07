lista = []
menor = 0
maior = 0
for c in range(0, 5):
    lista.append(int(input(f'Digite um Valor para a posição {c}: ')))
    if c == 0:
        menor = lista[c]
        maior = lista[c]
    if menor > lista[c]:
        menor = lista[c]
    if maior < lista[c]:
        maior = lista[c]
print('-=' * 40)
print(f'Você digitou os valores: {lista}')
print(f'O menor valor foi {menor} encontrado na posição: ', end='')

for c in range(0,5):
    if lista[c] == menor:
        print(c, end='... ')
print()
print(f'O maior valor foi {maior} encontrado na posição: ', end='')
for c in range(0, 5):
    if lista[c] == maior:
        print(c, end='... ')