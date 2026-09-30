n = s = cont = 0
while True:
    n = int(input('Digite um valor (999 para parar): '))
    if n == 999:
        break
    s += n
    cont += 1
print(f'A soma dos \033[1;31m{cont}\033[m valores foi \033[1;32m{s}\033[m')