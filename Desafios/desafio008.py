metro = int(input('Fale uma quantidade de metros:'))
cen = metro*100
mil = metro*1000
print('\033[1;35m{}\033[m em centímetros vale \033[1;32m{}\033[m e em milímetros vale \033[1;31m{}\033[m'.format(metro, cen, mil))