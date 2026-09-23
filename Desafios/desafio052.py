num = int(input('Digite um Valor:'))
div = 0
for c in range(1, num+1):
    res = num % c
    if res == 0:
        div = div+1
if div == 2:
    s = 'Primo'
else:
    s = 'Não é um primo'
print('{} é um número {}'.format(num, s))