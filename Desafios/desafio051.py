num = int(input('Primeiro Termo: '))
raz = int(input('Razão: '))
print(num)
for c in range(0, 10):
    res = num + raz
    num = res
    print(res)