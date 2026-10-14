lista = list()
dado = dict()
med = 0
while True:
    nome = str(input('Nome: '))
    dado['nome'] = nome
    sexo = str(input('Sexo: [M/F] '))
    if sexo != 'M' and sexo != 'F':
        while True:
            sexo = str(input('Resposta Inválida. Digite Novamente: [M/F]')).upper().strip()
            if sexo == 'M' or sexo == 'F':
                break
    dado['sexo'] = sexo
    id = int(input('Idade: '))
    dado['idade'] = id
    if len(lista) == 0:
        med = id
    else:
        med += id
    lista.append(dado.copy())
    pros = input('Quer Continuar: [S/N]').upper().strip()
    if pros != 'S' and pros != 'N':
        while True:
            pros = input('Reposta Inválida. Digite Novamente: [S/N]').upper().strip()
            if pros == 'S' or pros == 'N':
                break
    if pros == 'N':
        break
mi = med / len(lista)
print(f'- O grupo tem {len(lista)} pessoas\n- A média é de {mi:5.2f} anos')
print(f'- As mulheres cadastradas foram', end='')
for p in lista:
    if p['sexo'] == 'F':
        print(f' {p["nome"]}', end='')
print()
print('- Lista das pessoas que estão acima da média')
for p in lista:
    if p['idade'] >= mi:
        print('  ', end='')
        for k, v in p.items():
            print(f'{k} = {v};', end='')
        print()
print('<< ENCERRADO >>')