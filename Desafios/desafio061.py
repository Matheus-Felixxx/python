r = 0
num = int(input('Primeiro Termo: '))
raz = int(input('Razão: '))
print(num)
while r != 10:
    res = num + raz
    num = res
    print(res)
    r +=1