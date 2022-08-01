import time
from random import randint
print('-=-'*25)
print('Vou pensar em um numero de 0 a 5. Tente adivinhar...')
print('-=-'*25)
pc = randint(0, 5)
n = int(input('Em que numero eu pensei? '))
print('PROCESSANDO...')
time.sleep(3)
if pc == n:
    print('Parabens! Você conseguiu me vencer!')
else:
    print(f'Ganhei eu pensei no numero {pc} e não no {n}!')