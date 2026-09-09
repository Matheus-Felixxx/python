num = int(input('digite um valor:'))
dob = num * 2
tri = num * 3
rq = num ** (1/2)
print('Seu número é \033[1;31m{}\033[m. O dobro dele é \033[1;33m{}\033[m. O triplo dele é \033[1;32m{}\033[m. A raiz quadrada dele é \033[1;36m{}\033[m'.format(num, dob, tri, rq))