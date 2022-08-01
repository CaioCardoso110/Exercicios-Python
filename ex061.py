print('=-' * 10 ,'\nGerador de PA')
print('=-' * 10)
t = int(input('Primeiro termo: '))
r = int(input('Razão: '))
c = 0
print(f'{t}', end='')
while not c == 9:
    c += 1
    t += r
    print(end=' -> ' f'{t}')
print(end=' FIM ')
