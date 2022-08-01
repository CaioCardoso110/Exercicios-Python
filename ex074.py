from random import randint
n = tuple(randint(1, 10) for c in range(1, 6))
print(f'Os valores sorteado foram: {n}')
print(f'O maior valor sorteado foi {max(n)}')
print(f'O menor valor sorteado foi {min(n)}')
