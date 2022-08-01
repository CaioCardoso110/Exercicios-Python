from time import sleep
from random import randint, choice
print('''Suas opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
itens = ['PEDRA', 'PAPEL', 'TESOURA']
o = int(input('Qual é a sua jogada? '))
pc = randint(0, 2)
print('JO')
sleep(0.5)
print('KEN')
sleep(0.5)
print('PO!!!')
sleep(0.5)
print('=-' * 20)
print(f'Computador jogou {itens[pc]}')
print(f'Jogador jogou {itens[o]}')
print('-=' * 20)
if o == pc:
    print('EMPATE')
elif o == 0 and pc == 2 or o == 1 and pc == 0 or o == 2 and pc == 1:
    print('JOGADOR VENCE')
else:
    print('COMPUTADOR VENCE')
