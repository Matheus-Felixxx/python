import math
n1 = float(input('Qual sua primeira nota: '))
n2 = float(input('Qual sua segunda nota: '))
med = (n1 + n2) / 2
if med < 5.0:
    print('\033[0;31mREPROVADO!!!\033[m')
elif med == 5.0 or med == 6.9:
    print('\033[0;33mRECUPERAÇÃO!!!\033[m')
elif med >= 7.0:
    print('\033[0;32mAPROVADO!!!\033[m')