time = ('Flamengo', 'Palmeiras', 'Athletico Paranaense', 'Fluminense',
        'Bahia', 'Cruzeiro', 'Atlético Mineiro', 'Santos', 'Coritiba',
        'Red Bull Bragantino', 'São Paulo', 'Botafogo', 'Vitória',
        'Corinthians', 'Mirassol', 'Vasco da Gama', 'Grêmio',
        'Internacional', 'Remo', 'Chapecoense')
print(f'Lista de times do Brasileirão: {time}')
print('=-'*40)
print(f'Os 5 primeiros são: {time[0:5]}')
print('=-'*40)
print(f'Os 4 últimos são: {time[-5:-1]}')
print('=-'*40)
print(f'Time em ordem Alfabética: {sorted(time)}')
print('=-'*40)
print(f'O Chapecoense está na {time.index('Chapecoense') + 1}º posição')