num = int(input('Digite um número inteiro: '))
opc = int(input('Escolha a base de conversão: '))
if opc == 1:
    print(bin(num))
elif opc == 2:
    print(oct(num))
elif opc == 3:
    print(hex(num))
else:
    print('Opção Inválida')