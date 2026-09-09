real = float(input('Quantos reais você tem?'))
dolar = real/5.16
print('Você tem \033[0;31mR${}\033[m, você pode comprar \033[1;33m${:.2f}\033[m de dólares'.format(real,dolar))