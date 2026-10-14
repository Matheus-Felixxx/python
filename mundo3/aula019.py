# pessoas = {'nome': 'Matheus', 'idade': 15, 'sexo': 'M'}
# pessoas['peso'] = 98.5
# for k, v in pessoas.items():
#     print(f'{k} = {v}')

# brasil = []
# estado = {'uf':'Rio de Janerio', 'sigla': 'RJ'}
# estado2 = {'uf':'São Paulo', 'sigla': 'SP'}
# brasil.append(estado)
# brasil.append(estado2)
#
# print(brasil[0])

estado = dict()
brasil = list()
for c in range(0, 3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla do Estado: '))
    brasil.append(estado.copy())
for e in brasil:
    for v in e.values():
        print(v, end=' ')
    print()