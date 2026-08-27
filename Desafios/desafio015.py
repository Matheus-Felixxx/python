d = int(input('Quantos dias esse carro foi alugado? '))
km = float(input('Quantos km foram rodados? '))
rf = (d*60)+(km*0.15)
print('O valor total a ser pago é R${:.2f}'.format(rf))