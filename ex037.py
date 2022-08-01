n = int(input('Digite um numero inteiro: '))
print('Escolha uma das bases para conversão: ')
print('[ 1 ] coverter para BINARIO\n[ 2 ] converter para OCTAL \n[ 3 ] coverter para HEXADECIMAL')
o = int(input('Sua opção: '))
if o == 1:
    print(f'{n} convertido para BINÁRIO é igual a {bin(n)[2:]}')
elif o == 2:
    print(f'{n} convertido para OCTAL é igual a {oct(n[2:])}')
elif o == 3:
    print(f'{n} convertido para HEXADECIMAL é igual a {hex(n[2:])}')
else:
    print('Tente de novo')

