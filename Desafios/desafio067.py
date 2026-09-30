n = c = s = 0
while True:
    print('-' * 40)
    n = int(input('Quer ver a tabuada de qual valor? '))
    print('-' * 40)
    if n < 0:
        break
    c += 1
    for c in range(0, 11):
        s = n * c
        print('-' * 40)
        print(f'{n} x {c} = {c}')
print('=' * 40)
print('PROGRAMA TABUADA ENCERRADO. Volte sempre!')
print('=' * 40)