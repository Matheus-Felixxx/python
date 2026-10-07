lista = []
par = []
impar = []
while True:
    v = int(input('Digite um número: '))
    if v % 2 == 0:
        lista.append(v)
        par.append(v)
    else:
        lista.append(v)
        impar.append(v)
    r = input('Quer Continuar? [S/N]').upper()
    if r == 'N':
        break
print(f'A lista completa é: {lista}')
print(f'A lista de pares é: {par}')
print(f'A lista de ímpares é: {impar}')