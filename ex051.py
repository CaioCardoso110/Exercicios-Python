print('=' * 20)
print('Termos de uma PA')
print('=' * 20)
t = int(input('Primeiro Termo: '))
r = int(input('Razão: '))
print(f'{t}', end='')
for c in range(1, 10):
    t += r
    print(end=' -> ' f'{t}')
print(end=' -> ACABOU')
