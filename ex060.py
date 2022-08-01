from math import factorial
tot = 0
n = int(input('Digite um numero para calcular seu fatorial: '))
print(f'Calculando {n}! = {n}', end='')
tot = factorial(n)
while not n == 1:
    n -= 1
    print(f' x {n}', end='')
print(' = ', end='')
print(f'{tot}', end='')
