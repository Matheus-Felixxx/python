# a = 3
# b = 4
# print('Os valores são \033[32m{}\033[m e \033[31m{}\033[m!!!'.format(a,b))

# nome = input('Qual seu nome? ')
# print('Olá! Muito prazer em te conhecer, {}{}{}!!!!'.format('\033[4;35m', nome, '\033[m'))

nome = input('Qual seu nome? ')
cores = {'Limpa':'\033[m', 'azul':'\033[1;34m', 'roxo':'\033[4;35m', 'pretoebranco':'\033[7;30m'}
print('Olá! Muito prazer em te conhecer, {}{}{}!!!!'.format(cores['azul'], nome, cores['Limpa']))