def linha():
    print('-' * 40)


print('CONTROLE DE TERRENOS')
linha()

larg = float(input('LARGURA (m): '))
comp = float(input('COMPRIMENTO (m): '))
def mult(a, b):
    tot = a * b
    print(f'A aréa de um terreno {larg} x {comp} é de {tot}m²')

mult(larg, comp)