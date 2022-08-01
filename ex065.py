n = s = maior = c = m = 0
p = 's'
menor = 99999
while p != 'n':
    n = int(input('Digite um número: '))
    p = str(input('Você quer continuar? [S/N]: '))
    s += n
    c += 1
    m = s / c
    if n > maior:
        maior = n
    if n < menor:
        menor = n
print(f'Você digitou {c} números e a média foi {m:.2f}')
print(f'O maior valor foi {maior} e o menor foi {menor}')
