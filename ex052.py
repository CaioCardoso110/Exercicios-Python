d = 0
n = int(input('Digite um numero: '))
for c in range(1, n+1):
    if n % c == 0:
        d += 1
        print(f'\033[0;33m{c}\033[m', end=' ')
    else:
        print(f'\033[0;31m{c}\033[m', end=' ')
if d > 2:
    print(f'\nO numero {n} foi dividido {d} vezes')
    print('Por isso ele nao é PRIMO')
else:
    print(f'\nO numero {n} foi dividido {d} vezes')
    print('Por isso ele é PRIMO')
