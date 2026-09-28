num = int(input('Escreva um valor:'))
n2 = num
r = 0
r1 = 1
s = 0
print(s)

while n2 != 1:
    s = r + r1
    r = r1
    r1 = s
    print(s)
    n2 -= 1