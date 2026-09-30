md = mv = hc = 0
i = 0
sex = ''
p = ''

while True:
    print('=' * 40)
    print('CADASTRE UMA PESSOA')
    print('=' * 40)
    i = int(input('Idade: '))
    print('-' * 40)
    #Pergunta o Sexo da pessoa e pergunta repetidas vezes caso esteja errado
    sex = input('Sexo: [M/F]').upper()
    print('-' * 40)
    while sex != 'M' and sex != 'F':
        sex = input('Sexo: [M/F]').upper()
        print('-' * 40)
    if i > 18:
        md += 1
    if sex == 'M':
        hc += 1
    if i < 20 and sex == 'F':
        mv += 1
    # Pergunta se quer continuar
    p = input('Quer continuar? [S/N]').upper()
    print('-' * 40)
    while p != 'S' and p != 'N':
        p = input('Quer continuar? [S/N]').upper()
        print('-' * 40)
    if p == 'N':
        break
print('=' * 40)
print(f'Total de Pessoas com mais de 18 anos: {md}\nTotal de Homens cadastrados: {hc}\nTotal de mulheres com menos de 20 anos: {mv}')
print('=' * 40)