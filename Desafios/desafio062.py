num = int(input('Primeiro Termo: '))
raz = int(input('Razão: '))
r = int(input('Quantos termos você quer mostrar?'))
print(num)
while r !=0:
    res = num + raz
    num = res
    print(res)
    r -= 1
    if r == 0:
        r = int(input('Quantos termos você quer mostrar?'))