aluno = {}
nome = input('Nome: ')
med = float(input(f'Média de {nome}: '))
sit = 'nada'
if med >= 7.0:
    sit = 'Aprovado'
else:
    sit = 'Reprovado'
aluno['Nome'] = nome
aluno['Media'] = med
aluno['Situação'] = sit
for k, v in aluno.items():
    print(f'{k} = {v}')