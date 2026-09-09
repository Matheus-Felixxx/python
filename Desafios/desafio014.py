c = float(input('Digite a temperatura em ºC:'))
f= 9*c/5+32
print('Seu temperatura em graus Celsius é \033[1;31m{}\033[m ºC e em grau Fahrenheit é \033[1;36m{}\033[m ºF'.format(c,f))