r = str(input('Digite seu sexo:')).upper()

while r != 'M' and r != 'F':
    print('Valor Inválido!')
    r = str(input('Digite Novamente [M/F]')).upper()
if r == 'M':
    print('Você é um homem. Seu sexo foi registrado.')
elif r == 'F':
    print('Você é uma mulher. Seu sexo foi registrado')

