print('-' * 23)
print('SEQUÊNCIA DE FIBONACCI')
print('-' * 23)
t = int(input('Quantos termos você quer mostrar? '))
n1 = 0
n2 = 1
fibo = 0
cont = 0
while not cont == t:
    cont += 1
    fibo = n1 + n2
    n1 = n2
    n2 = fibo
    print(f'{fibo}', end=' → ')
print(end='ACABOU')
