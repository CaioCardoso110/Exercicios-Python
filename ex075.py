n1 = int(input('Digite um numero: '))
n2 = int(input('Digite outro numero: '))
n3 = int(input('Digite mais um numero: '))
n4 = int(input('Digite o último numero: '))
tupla = n1, n2, n3, n4
nine = 0
print('Você digitou os valores: ', end='')
for c in tupla:
    print(f'{c} ', end='')
    if c == 9:
        nine += 1
print(f'\nO valor 9 apareceu {nine} vezes')
if 3 in tupla:
    print(f'O valor 3 apareceu na {tupla.index(3) + 1}° posição')
else:
    print('O valor 3 Não foi digitado em nenhuma posição!')
print(f'Os valores pares digitados foram ', end='')
for c1 in tupla:
    if c1 % 2 == 0:
        print(f'{c1}', end=' ')
