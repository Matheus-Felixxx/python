num = int(input('Digite um número de 0 a 9999:'))
uni = num % 10
dez = (num // 10) % 10
cen = (num // 100) % 10
mil = (num // 1000) % 10
print('Seu número possui {} de unidade, {} de dezena, {} de centena e {} de milhar'.format(uni, dez, cen, mil))