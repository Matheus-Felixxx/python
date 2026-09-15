casa = int(input('Qual o valor da sua casa? '))
sal = int(input('Qual seu salário? '))
anos = int(input('Enquanto anos você pretende pagar esse empréstimo? '))
pres = casa / (anos * 12)
lim = sal * 30 / 100
mes = anos * 12
if pres > lim:
    print('\033[0;31m EMPRÉSTIMO NEGADO!!! \033[m')
else:
    print('Seu empréstimo foi \033[0;32maprovado\033[m, você vai pagar R${:.2f} por {} meses'.format(pres, mes))