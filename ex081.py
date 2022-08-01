lista = []
while True:
    lista.append(int(input('Digite um valor: ')))
    res = str(input('Você quer continuar? [S/n] ')).upper()[0]
    while 'Ss' in res:
        res = str(input('Dado invalido. Tente novamente. Você quer continuar? [S/n] ')).upper()[0]
    if 'N' in res:
        break
print('=' * 30)
print(f'Você Digitou {len(lista)} elementos')
lista.sort(reverse=True)
print(f'Os valores em ordem decrescente são {lista}')
if 5 in lista:
    print('O valor 5 faz parte da lista!')
else:
    print('O valor 5 nao faz parte da lista')
