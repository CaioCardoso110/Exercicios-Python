print('-=-' * 15)
print('Analisador de Triângulos!')
print('-=-' * 15)
n1 = float(input('Primeiro segmento: '))
n2 = float(input('Segundo segmento: '))
n3 = float(input('terceiro segmento: '))
if n1 < n2 + n3 and n2 < n3 + n1 and n3 < n1 + n2:
    print('Os segmentos acima PODEM FORMAR um triângulo!')
else:
    print('Os segmentos acima NÂO PODEM  FORMAR  um triâgulo!')
