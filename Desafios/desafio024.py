cidade = str(input('Qual o nome da sua cidade? ')).upper().strip()
div = cidade.split()[0]
print('sua cidade possui "Santo" no começo do nome?')
print('SANTO' in div)