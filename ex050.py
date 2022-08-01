s = 0
for c in range(1, 7):
    n = int(input(f'Digite {c}° numero: '))
    if n % 2 == 0:
        s += n
print(f'A soma de todos os numeros pares é {s}')
