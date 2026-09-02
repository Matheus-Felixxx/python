from gettext import find
frase = str(input('Digite uma frase: ')).upper().strip()
print('A letra "A" aparece {} vezes, ela aparece a primeira vez na posição {} e aparece a ultima vez na posição {}'.format(frase.count('A'), frase.find('A', 0), frase.rfind('A')))