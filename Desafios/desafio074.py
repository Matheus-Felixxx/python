from random import randint

num = tuple(randint(1, 9) for c in range(5))
print(f'Os valores sorteados foram: {num}')
print(f'O maior valor sorteado foi: {sorted(num)[-1]}')
print(f'O menor valor sorteado foi: {sorted(num)[0]}')