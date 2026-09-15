nome = input('Qual seu nome? ')
if nome == 'Matheus':
    print('Belo Nome!')
elif nome == 'Pedro' or nome == 'Maria' or nome == 'Paulo':
    print('Seu nome é bem popular no Brasil!')
elif nome in 'Ana Emanuelle Alice Juliana Yasmin':
    print('Belo nome feminino')
else:
    print('Seu nome é bem diferente!')
print('Tenha um bom dia {}'.format(nome))
