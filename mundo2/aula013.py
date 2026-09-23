# n1 = int(input('Digite um valor: '))
# n2 = int(input('Digite Outro Valor: '))
# n3 = int(input('Você quer que ele conte de quanto em quanto: '))
# for c in range(n1, n2+1, n3):
#     print(c)
# print('FIM!!!')

s = 0
for c in range(0, 4):
    n = int(input('Digite um valor: '))
    s += n
print('A soma de todos os valores é de {}'.format(s))