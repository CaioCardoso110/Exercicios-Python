while True:
    n = int(input('Quer ver a tabuada de qual valor? '))
    print('~' * 40)
    if n <= -1:
        break
    for c in range(1, 11):
        print(f'{n} x {c} = {n * c}')
print('PROGRAMA DE TABUADA ENCERRAADO. Volte sempre!')
