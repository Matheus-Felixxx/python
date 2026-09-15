peso = float(input('Qual seu peso? '))
al = float(input('Qual sua altura? '))
imc = peso / (al ** 2)
if imc < 18.5:
    print('Abaixo do Peso')
elif imc < 25:
    print('Peso ideal')
elif imc < 30:
    print('Sobrepeso')
elif imc < 40:
    print('Obesidade')
else:
    print('Obesidade mórbida')
