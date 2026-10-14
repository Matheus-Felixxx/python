from random import randint
from time import sleep

dado = {}
jogador = list()
num = 0

print('Valores sorteados: ')
for c in range(0, 4):
    dado['jogador'] = f'Jogador {c + 1}'
    dado['num'] = randint(1, 6)
    jogador.append(dado.copy())
    sleep(1)
    print(f'    Jogador{c + 1} tirou {dado['num']}')
dados = sorted(jogador, key=lambda item: item['num'], reverse=True)
print('Ranking dos jogadores: ')
for n, c1 in enumerate(dados, start=1):
    sleep(1)
    print(f'    {n}º lugar: {c1['jogador']} com {c1['num']}')