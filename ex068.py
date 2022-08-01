from random import randint
print('-=' * 30)
print('VAMOS JOGAR PAR OU IMPAR')
print('-=' * 30)
c = 0
while True:  # condição verdadeira
    pc = randint(1, 10)  # numero do pc
    n = int(input('Digite um valor de 1 a 10: '))  # numero do jogador
    while not n < 10:
        n = int(input('Valor invalido. Insira um numero de 1 a 10: '))
    j = str(input('Par ou Ímpar? [P/I]: ')).upper()   # resposta do jogador
    while j != 'P' and j != 'I':
        j = str(input('Opção invalida. Tente novamente. Par ou Ímpar? [P/I]: ')).upper()
    soma = n + pc
    print('=' * 50)
    print(f'Você jogou {n} e o computador {pc}. Total de {soma}.')
    print('=' * 50)
    if soma % 2 == 0 and j == 'P' or soma % 2 != 0 and j == 'I':
        print('Você GANHOU!\nVamos jogar novemente...')
        c += 1
    else:
        print('Você PERDEU!')
        print('=' * 50)
        break
print(f'GAME OVER! Voce ganhou {c} vez(es)')
