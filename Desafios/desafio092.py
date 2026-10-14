from datetime import date
dados = {}
data = date.today()
ano = data.year

nome = str(input('Nome: '))
dados['nome'] = nome
adn = int(input('Ano de Nascimento: '))
dados['idade'] = ano - adn
clt = int(input('Carteira de Trabalho (0 não tem): '))
dados['ctps'] = clt
if clt != 0:
    anc = int(input('Ano de contratação: '))
    dados['contratação'] = anc
    sal = float(input('Salário: R$'))
    dados['salário'] = sal
    dados['aposentadoria'] = (anc + 35) - adn

print(f'{dados}')
for k, v in dados.items():
    print(f'{k} tem o valor {v}')
