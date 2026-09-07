# nome = str(input('Qual é seu nome: ')) Condição simples
# if nome == 'Matheus':
#     print('Belo nome!')
# print('Bom dia, {}!'.format(nome))

# nome = str(input('Qual é seu nome: ')) Condição composta
# if nome == 'Matheus':
#     print('Belo nome!')
# else:
#     print('Seu nome é tão normal!')
# print('Bom dia, {}!'.format(nome))

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segundo nota: '))
m = (n1 + n2)/2
print('A sua média foi {:.1f}'.format(m))
print('PARABENS!' if m >= 6 else 'ESTUDE MAIS!!!!!!!') # Condição simplificada