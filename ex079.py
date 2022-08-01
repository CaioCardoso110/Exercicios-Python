lista = []
while True:
    res = ''
    num = int(input('Digite um valor: '))
    if num not in lista:
        lista.append(num)
        print('Valor adicionado com sucesso!')
    else:
        print('Valor duplicado! Não vou adicionar...')
    res = str(input('Quer continuar? [S/N]: ')).upper()[0]
    while 'Ss' in res:
        res = str(input('Dado invalido. Tente novamente. Quer continuar? [N/S]: ')).upper()[0]
    if 'N' in res:
        break
print('=-' * 30)
lista.sort()
print(f'Você digitou os valores {lista}')
