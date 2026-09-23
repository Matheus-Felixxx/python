from datetime import date
maior = 0
menor = 0
hoje = date.today()
anoh = hoje.year
ano = 0
for c in range(0,7):
    ano = int(input('Ano de Nascimento:'))
    if anoh - ano >= 18:
        print('Maior de Idade')
        maior += 1
    elif anoh - ano < 18:
        print('Menor de Idade')
        menor += 1
print('Dentre os 7, {} são maiores de idade e {} são menores'.format(maior, menor))
