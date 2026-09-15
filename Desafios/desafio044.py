pre = float(input('Qual o preço a ser pago? '))
con = input('Qual a condição de pagamento (aperte o número da respectivo da condição de pagamento: 1 - à vista, 2 - à vista no cartão, 3 - 2x no cartão, 4 - 3x ou mais no cartão) ')
if con == '1':
    des = pre - (pre * 10 / 100)
    print('Você vai ganhar 10% de desconto! o preço vai ficar em R${}'.format(des))
elif con == '2':
    des = pre - (pre * 5 / 100)
    print('Você vai ganhar 5% de desconto! o preço vai ficar em R${}'.format(des))
elif con == '3':
    print('Você vai pagar o preço de R${}'.format(pre))
elif con == '4':
    au = pre + (pre * 20 / 100)
    print('Irá ter uma taxa de 20% de juros, o preço vai ficar em R${}'.format(au))
else:
    print('Opção inválida')