print('=-' * 10, '\nGerador de PA')
print('=-' * 10)
t = int(input('Primeiro termo: '))
r = int(input('Razão: '))
c = 0
mais = 10
total = 0
print(f'{t}', end='')
while mais != 0:
    total = total + mais
    while c <= total:
        c += 1
        t += r
        print(end=' → ' f'{t}')
    print(end=' PAUSA ')
    mais = int(input('\nQuantos termos você quer mostrar a mais? '))
print(f'Progressao finalizada com {total} termos')
