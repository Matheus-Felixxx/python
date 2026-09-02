nome = str(input('Digite seu nome completo: '))
print('Seu nome com letras maiúsculas fica: {0} \nSeu nome com letras minúsculas fica: {1} \nSeu nome possui {2} letras \ne o primeiro nome possui {3} letras'.format(nome.upper(), nome.lower(), len(nome.replace(' ', '')), len(nome.split()[0])))
