lista = []
while True:
    v = int(input('Digite um valor: '))
    num = v
    if num in lista:
        print('Esse número ja foi adicionado')
        c = input('Quer continuar? [S/N] ').upper()
        if c == 'N':
            break
    else:
        print('Número adicionado com sucesso!')
        lista.append(v)
        c = input('Quer continuar? [S/N] ').upper()
        if c == 'N':
            break
print('-=' * 40)
lista.sort()
print(f'Os valores digitados foram: {lista}')