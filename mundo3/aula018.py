# lista = list()
# lista.append('Gustavo')
# lista.append(40)
# lista1 = list()
# lista1.append(lista[:])
# lista[0] = 'Matheus'
# lista[1] = 20
# lista1.append(lista[:])
# print(lista1)

# pessoa = [['Emanuelle', 16], ['Matheus', 15], ['Gabriel', 15], ['Alice', 16]]
# for p in pessoa:
#     print(f'{p[0]} tem {p[1]} anos')

pessoa = list()
dado = list()
c = 0
maior = menor = 0
while True:
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    pessoa.append(dado[:])
    dado.clear()
    c += 1
    if c == 3:
        break
for p in pessoa:
    if p[1] >= 21:
        print(f'{p[0]} é maior de idade')
        maior += 1
    else:
        print(f'{p[0]} é menor de idade')
        menor += 1
print(f'Temos {menor} pessoas de menor e {maior} pessoas de maior')