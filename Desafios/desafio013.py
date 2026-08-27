si = float(input('Qual seu salário?'))
au = int(input('Você vai receber'))
mul = si*au
div = mul/100
sf = si+div
print('Se você receber um aumento de {}% seu salário vai para R${}'.format(au,sf))