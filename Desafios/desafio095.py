time = list()
jogador = {}
gols = list()
total = 0
while True:
    jogador.clear()
    nome = input('Nome do Jogador: ')
    jogador['nome'] = nome
    part = int(input(f'Quantas partidas {nome} jogou? '))
    gols.clear()
    for c in range(0, part):
        gols.append(int(input(f'Quantos gols na partida {c + 1}? ')))
        jogador['gols'] = gols.copy()
        if c == 0:
            total = gols[0]
        else:
            total += gols[c]
    jogador['total'] = total
    time.append(jogador.copy())
    resp = input('Quer continuar? [S/N]').upper()[0]
    if resp != 'S' and resp != 'N':
        while True:
            resp = input('ERRO! RESPONDA APENAS S OU N. ').upper()
            if resp == 'S'  or resp == 'N':
                break
    if resp == 'N':
        break
print('-=' * 30)
print('cod', end='')
for i in jogador.keys():
    print(f'{i:<15}', end='')
print()
print('-' * 40)
for k, v in enumerate(time):
    print(f'{k:>3}', end='')
    for d in v.values():
        print(f' {str(d):<15}', end='')
    print()
print('-' * 40)
while True:
    busca = int(input('Mostrar dados de qual jogador? [999 para parar]: '))
    if busca == 999:
        break
    if busca >= len(time):
        print(f'ERRO! Não existe jogador com o código {busca}')
    else:
        print(f'--- LEVANTAMENTO DO JOGADOR {time[busca]["nome"]}')
        for i, g in enumerate(time[busca]["gols"]):
            print(f'    No jogo {i + 1} fez {g}.')
    print('-' * 40)
print('<< Volte Sempre >>')