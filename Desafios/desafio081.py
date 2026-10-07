lista = []
while True:
    v = int(input('Digite um Valor: '))
    lista.append(v)
    r = input('Quer continuar? [S/N]').upper()
    if r == 'N':
        break
lista.sort(reverse=True)
print(f'Você digitou {len(lista)}\nOs valores em ordem decrescente são: {lista}')
if 5 in lista:
    print(f'O valor 5 foi encontrado na lista na posição: {lista.count(5) + 1}!')
else:
    print('O valor 5 não foi encontrado na lista!')