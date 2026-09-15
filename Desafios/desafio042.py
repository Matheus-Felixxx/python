n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro valor: '))
n3 = int(input('Digite outro valor: '))
if n1 + n2 > n3:
    print('É possível formar um triângulo com essas três medidas')
    if n1 == n2 and n1 == n3 and n2 == n3:
        print('Seu triângulo é Equilátero')
    elif n1 == n2 or n1 == n3 or n2 == n3:
        print('Seu triângulo é Isósceles')
    else:
        print('Seu triângulo é Escaleno')
else:
    print('Não é possível formar um triângulo com essas três medidas')