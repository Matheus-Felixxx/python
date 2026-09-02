nome = str(input('Digite seu nome completo:')).strip()
print('O seu primeiro nome é {0} e o último é {1}'.format(nome.split()[0], nome.split()[-1]))