print('-' * 40)
print('LOJAS SUPER BARATÃO')
print('-' * 40)
soma = 0
caro = 0
barato = 0
menor = ''
cont = 1
while True:
    produto = str(input('Nome do produto: '))
    preco = int(input('Preço: R$'))
    soma += preco
    if preco >= 1000:
        caro += 1
    if cont == 1:
        barato = preco
        menor = produto
    else:
        if preco < barato:
            barato = preco
            menor = produto
    r = ' '
    while r not in 'SN':
        r = str(input('Quer Continuar? [S/N] ')).strip().upper()[0]
        cont += 1
    if r == 'N':
        break
print('-' * 10, 'FIM DO PROGRAMA', '-' * 10)
print(f'O total da compra foi R${soma:.2f}')
print(f'Temos {caro} produtos custando mais de R$1000.00')
print(f'O produto mais barato foi {menor} que custa R${barato}')
