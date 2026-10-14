jogador = {}
gols = []
total = 0
nome = input('Nome do Jogador: ')
jogador['nome'] = nome
part = int(input(f'Quantas partidas {nome} jogou? '))
for c in range(0, part):
    gols.append(int(input(f'Quantos gols na partida {c + 1}? ')))
    jogador['gols'] = gols.copy()
    if c == 0:
        total = gols[0]
    else:
        total += gols[c]
jogador['total'] = total
print(jogador)
print('-=' * 30)
for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}.')
print('-=' * 30)
print(f'O jogador {nome} jogou {part}')
for n, v1 in enumerate(gols):
    print(f'    => Na partida {n + 1}, fez {v1} gols.')
print(f'Foi um total de {jogador["total"]}')