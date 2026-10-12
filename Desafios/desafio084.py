pessoa = list()
dados = list()
cont = pma = pme = 0
while True:
    # Coleta os dados necessários
    dados.append(str(input('Nome: ')))
    dados.append(float(input('Peso: ')))
    pessoa.append(dados[:])
    cont += 1
    dados.clear()


    # Pega o maior peso
    if cont - 1 == 0:
        pma = pessoa[0][1]
        pme = pessoa[0][1]
    if pma < pessoa[-1][1]:
        pma = pessoa[-1][1]
    if pme > pessoa[-1][1]:
        pme = pessoa[-1][1]


    #Continuar ou Parar o Loop:
    p = input('Quer continuar? [S/N]').upper().strip()
    while p != 'S' and p != 'N':
        p = input('A resposta é invalida! Digite Novamente: [S/N]')
    if p == 'N':
        break

print(f'Você Cadastrou {cont} pessoas')
print(f'O maior peso foi {pma}. Peso de ', end='')
for c in range(0, len(pessoa)):
    if pessoa[c][1] == pma:
        print(pessoa[c][0], end='. ')
print()
print(f'O menor peso foi {pme}. Peso de ', end='')
for c1 in range(0, len(pessoa)):
    if pessoa[c1][1] == pme:
        print(pessoa[c1][0], end='. ')
