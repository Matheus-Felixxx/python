p = 0
np = ''
t = 0
mm = 0
mn = ''
mp = 0

while True:
    print('-' * 40)
    #Verifica o nome e preço do produto
    np = input('Nome do Produto: ')
    p = float(input('Preço: R$'))
    t += p
    if p > 1000:
        mm += 1
    if mn == '':
        mp = p
        mn = np
    else:
        if mp > p:
            mp = p
            mn = np
    #Pergunta se quer continuar
    c = input('Quer continuar? [S/N]').upper()
    while c != 'S' and c != 'N':
        c = input('Quer continuar? [S/N]').upper()

    if c == 'N':
        break
print('=' * 40)
print('FIM DO PROGRAMA')
print('=' * 40)
print('-' * 40)
print(f'O total da compra foi R${t:.2f}\nTemos {mm} produtos custando mais de R$1000\nO produto mais barato foi {mn} que custa {mp:.2f}')
print('-' * 40)