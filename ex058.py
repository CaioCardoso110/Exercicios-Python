from random import randint
chance = 0
pc = randint(1, 10)
print('''Sou seu computador...
Acabei de pensar em numero entre 0 e 10.
Será que você consegue adivinhar qual foi?''')
jogador = int(input('Qual o seu palpite? '))
while jogador != pc:
    if pc < jogador:
        print('Menos... tente mais uma vez.')
        jogador = int(input('Qual o seu palpite?'))
    else:
        print('Mais... Tente mais uma vez')
        jogador = int(input('Qual o seu palpite? '))
    chance += 1
print(f'Acertou com {chance} tentativa(s). Parabens!')
