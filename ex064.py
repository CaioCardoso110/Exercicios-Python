n = c = s = 0
while n != 999:
    n = int(input('Digite um numero [999 para parar]: '))
    if n != 999:
        s += n
        c += 1
print(f'Você digitoui {c} números e a soma entre eles foi {s}.')
