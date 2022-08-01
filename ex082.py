lista = []
pares = []
impares = []
while True:
    lista.append(int(input('Digite um valor: ')))
    res = str(input('Você quer continuar? [S/N] ')).upper()[0]
    while 'Ss' in res:
        res = str(input('Dado invalido. Tente novamente. Você quer contiuar? [S/N] ')).upper()[0]
    if 'N' in res:
        break
print('=-' * 30)
for poicao, valores in enumerate(lista):
    if valores % 2 == 0:
        pares.append(valores)
    else:
        impares.append(valores)
print(f'A lista completa é {lista}')
print(f'A lista de pares é {pares}')
print(f'A lista de impares é {impares}')
