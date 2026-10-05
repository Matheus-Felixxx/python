palavras = {'aprender', 'programar', 'linguagem', 'python', 'curso', 'gratis', 'estudar', 'praticar', 'trabalho', 'mercado', 'programador', 'futuro'}

for c in palavras:
    print(f'Na Palavra {c.upper()} temos ', end= '' '')
    if c.count('a') > 0:
        print('A', end=' ')
    if c.count('e') > 0:
        print('E', end=' ')
    if c.count('i') > 0:
        print('I', end=' ')
    if c.count('o') > 0:
        print('O', end=' ')
    if c.count('u') > 0:
        print('U', end=' ')
    print()