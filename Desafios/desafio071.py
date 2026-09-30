p = c = v = d = u = 0

print('=' * 40)
print(f'{'BANCO CEV':^35}')
print('=' * 40)
while True:
     p = int(input('Que valor você quer sacar? R$'))
     c = p // 50
     p = p % 50
     v = p // 20
     p = p % 20
     d = p // 10
     p = p % 10
     u = p // 1
     if c > 0:
         print(f'Total de {c} cédulas de R$50')
     if v > 0:
         print(f'Total de {v} cédulas de R$20')
     if d > 0:
         print(f'Total de {d} cédulas de R$10')
     if u > 0:
         print(f'Total de {u} cédulas de R$1')
     print('=' * 40)
     break
print('Volte sempre ao BANCO CEV! Tenha um bom dia!')