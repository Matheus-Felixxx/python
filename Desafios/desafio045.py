import random
joken = input('Vamos jogar pedra, papel e tesoura. Escolha sua jogada: ').lower()
lista = ['pedra', 'papel', 'tesoura']
res = random.choice(lista)
if res == 'pedra' and joken == 'papel':
    print('Eu escolhi pedra e você papel. Você ganhou!!!')
elif res == 'pedra' and joken == 'tesoura':
    print('Eu escolhi pedra e você tesoura. Eu ganhei!!!')
elif res == 'tesoura' and joken == 'papel':
    print('Eu escolhi Tesoura e você Papel. Eu ganhei!!!')
elif res == 'tesoura' and joken == 'pedra':
    print('Eu escolhi Tesoura e você Pedra. Você ganhou!!!')
elif res == 'papel' and joken == 'pedra':
    print('Eu escolhi Papel e você Pedra. Eu ganhei!!!')
elif res == 'papel' and joken == 'tesoura':
    print('Eu escolhi Papel e você Tesoura. Você ganhou!!!')
else:
    print('Essa resposta não é válida')