vel = int(input('Qual a velocidade do seu carro?: '))
m1 = vel - 80
m2 = m1 * 7
if vel > 80:
    print('Você passou o limite de velocidade, você vai ser multado')
    print('Você tem que pagar R${} de multa!'.format(m2))
else:
    print('Você está dentro do limite de velocidade!')