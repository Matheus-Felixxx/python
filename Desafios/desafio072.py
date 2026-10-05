cont = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze', 'Doze', 'Treze', 'Quatorze', 'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')
r = int(input('Digite um número entre 0 e 20: '))
while r < 0 or r > 20:
    r = int(input('Tente novamente. Digite um número entre 0 e 20: '))
print(f'Você digitou o número {cont[r]}')