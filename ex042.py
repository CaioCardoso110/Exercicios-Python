print('-=-' * 15)
print('Analisador de triangulos 2.0')
print('-=-' * 15)
n1 = float(input('Primeiro segmento: '))
n2 = float(input('Segundo segmento: '))
n3 = float(input('Terceiro segmento: '))
if n1 < n2 + n3 and n2 < n1 + n3 and n3 < n1 + n2:
    print('Os segmentos acima PODEM FORMAR um triângulo ', end='')
    if n1 == n2 == n3:
        print('EQUILATERO')
    elif n1 == n2 != n3 or n2 == n3 != n1 or n1 == n3 != n2:
        print('ISÓSCELES')
    elif n1 != n2 != n3 and n2 != n1 != n3 and n3 != n2 != n1:
        print('ESCALENO')
else:
    print('Os segmentos acima NÃO PODEM FORMAR um triâgulo')
