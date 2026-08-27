vi = float(input('Digite o preço de um produto:'))
des = int(input('Digite o desconto desse produto:'))
mul = vi*des
div = mul/100
vf = vi-div
print('Seu produto com o desconto de {}% fica com o valor de R${}'.format(des,vf))