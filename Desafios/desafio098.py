from time import sleep

def linha():
    print('-=' * 40)


linha()
print('Contagem de 1 até 10 de 1 em 1')
for c in range(1, 11):
    print(c, end=' ')
    sleep(1)
print('FIM!')
linha()
print('Contagem de 10 até 0 de 2 em 2')
for c in range(10, -2, -2):
    print(c, end=' ')
    sleep(1)
print('FIM!')
linha()
print('Agora é sua vez de personalizar a contagem!')
ini = int(input('Início: '))
fim = int(input('Fim: '))
pas = int(input('Passo: '))
linha()
def perso(a, b, c):

    if ini > fim and pas > 0:
        print(f'Contagem de {ini} até {fim} de {pas} em {pas}')
        for c in range(ini, fim + 1, -pas):
            print(c, end=' ')
            sleep(1)
    if ini < fim and pas < 0:
        for c in range(ini, fim -1 , (pas * -2) + pas):
            print(c, end=' ')
            sleep(1)
    if ini < fim and pas == 0:
        print(f'Contagem de {ini} até {fim} de {pas + 1} em {pas + 1}')
        for c in range(ini, fim + 1, 1):
            print(c, end=' ')
            sleep(1)
    if ini > fim and pas == 0:
        print(f'Contagem de {ini} até {fim} de {pas + 1} em {pas + 1}')
        for c in range(ini, fim - 1, -1):
            print(c, end=' ')
            sleep(1)
    if ini < fim and pas > 0:
        for c in range(ini, fim + 1, pas):
            print(c, end=' ')
            sleep(1)
    if ini > fim and pas < 0:
        for c in range(ini, fim - 1, pas):
            print(c, end=' ')
            sleep(1)
    print('FIM!')
perso(ini, fim, pas)