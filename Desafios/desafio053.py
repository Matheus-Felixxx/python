p = input('Digite uma palavra: ')
p = p.replace(' ', '')
inv = p[::-1]

if inv == p:
    print('Sua Frase é um palíndromo')
else:
    print('Sua Frase não é um palíndromo')
    