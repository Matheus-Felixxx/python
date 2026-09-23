si = 0
mi = 0
hv = 0
m = 0

for c in range(0, 4):
    nome = input('nome: ')
    ida = int(input('Idade: '))
    sexo = input('Sexo [M/F]: ')
    si = si + ida
    if sexo == 'M' and ida > mi:
        hv = nome
        mi = ida
    if sexo == 'F' and ida < 20:
        m += 1
media = si / 4
print('A media das idades é {}, o homem com maior idade é {} e ele tem {} anos. {} mulheres são menores de 20'.format(media, hv, mi, m))