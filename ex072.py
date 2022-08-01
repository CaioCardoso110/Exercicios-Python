numeros = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete',
           'oito', 'nove', 'dez', 'onze', 'dozse', 'treze', 'catorze', 'quinze', 'dezesseis',
           'dezessete', 'dezoito', 'dezenove', 'vinte')
while True:
    res = ''
    n = int(input('Digite um numero entre 0 e 20: '))
    while n > 20 or n < 0:
        n = int(input('Tente novamente. Digite um numero entre 0 e 20: '))
    print(f'Você digitou o numero {numeros[n]}')
    res = str(input('Você quer Continuar? [S/N] ')).upper()[0]
    if res == 'N':
        break
