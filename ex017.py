from math import hypot
n1 = float(input('Comprimento do cateto oposto: '))
n2 = float(input('Comprimento do cateto adjacente: '))
print(f'A hipotenusa vai medir {hypot(n1, n2):.2f}')
