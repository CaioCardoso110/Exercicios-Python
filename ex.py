num = []
for n in range(0, 5):
    num.append(int(input(f'Digite um valor para a posição {n}: ')))
for c in enumerate(num):
    print(c)
