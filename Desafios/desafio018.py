import math
num = float(input('Digite um número: '))
cos = math.cos(math.radians(num))
tan = math.tan(math.radians(num))
son = math.sin(math.radians(num))
print('O seno do seu ângulo é {}, o cosseno é {} e a tangente é {}'.format(son, cos, tan))