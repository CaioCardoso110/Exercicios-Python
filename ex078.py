num = []
for n in range(0, 5):
    num.append(int(input(f'Digite um valor para a posição {n}: ')))
print('=-' * 30)
print(f'Você digitou os valores {num}')
print(f'O maior valor digitado foi {max(num)} nas posições ', end='')
for p, v in enumerate(num):
    if v == max(num):
        print(f'{p}...', end='')
print(f'\nO menor valor digitado foi {min(num)} nas posições ', end='')
for p, v in enumerate(num):
    if v == min(num):
        print(f'{p}...', end='')
