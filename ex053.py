frase = str(input('Digite uma frase: ')).upper()
sep = frase.split()
junto = ''.join(sep)
inverso = ''.join(reversed(junto))
print(f'O inverso de {junto} é {inverso}')
if junto == inverso:
    print('A frase digitada é um polindromo!')
else:
    print('A frase digitada não é um polindromo!')
