dis = int(input('Qual a distância da sua viagem'))
if dis <= 200:
    p1 = 0.50 * dis
    print('Sua viagem vai custar R${:.2f}'.format(p1))
else:
    p2 = 0.45 * dis
    print('A empresa possui um desconto para viagem acima de 200km, agora será cobrado R$0,45 por Km')
    print('Sua viagem vai custar R${:.2f}'.format(p2))