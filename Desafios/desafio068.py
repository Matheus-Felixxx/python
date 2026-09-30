from random import randint

n = v = 0
pi = ''
ran = randint(0,10)
print('=' * 40)
print('VAMOS JOGAR PAR OU ÍMPAR')
print('=' * 40)
while True:
    n = int(input('Diga um valor: '))
    pi = input('Par ou Ímpar? [P/I] ').upper()
    if (n + ran) % 2 == 0 and pi == 'P':
        print('-' * 40)
        print(f'Você jogou {n} e o computador {ran}. total de {n + ran} DEU PAR')
        print('=' * 40)
        print('Você Venceu!!!')
        print('=' * 40)
        print('Vamos jogar novamente...')
        print('-' * 40)
        v += 1
    if (n + ran) % 2 > 0 and pi == 'I':
        print('-' * 40)
        print(f'Você jogou {n} e o computador {ran}. total de {n + ran} DEU ÍMPAR')
        print('=' * 40)
        print('Você Venceu!!!')
        print('=' * 40)
        print('Vamos jogar novamente...')
        print('-' * 40)
        v += 1
    if (n + ran) % 2 > 0 and pi == 'P':
        print('-' * 40)
        print(f'Você jogou {n} e o computador {ran}. total de {n + ran} DEU ÍMPAR')
        print('=' * 40)
        print('Você perdeu!!!')
        print('=' * 40)
        print('-' * 40)
        break
    if (n + ran) % 2 == 0 and pi == 'I':
        print('-' * 40)
        print(f'Você jogou {n} e o computador {ran}. total de {n + ran} DEU PAR')
        print('=' * 40)
        print('Você perdeu!!!')
        print('=' * 40)
        print('-' * 40)
        break
print('#' * 40)
print(f'GAME OVER! Você venceu {v} vezes')
print('#' * 40)