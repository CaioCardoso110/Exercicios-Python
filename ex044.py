print(('=' * 20), 'LOJAS CAIO', ('=' * 20))
valor = float(input('Valor das compras: R$'))
print('''FORMAS DE PAGAMENTO
[ 1 ] à vista no dinheiro/cheque
[ 2 ] à vista cartão
[ 3 ] 2x no cartão
[ 4 ] 3x no cartão ou mais''')
o = int(input('Qual é a opção? '))
if o == 1:
    print(f'Sua compra de R${valor:.2f} vai custar R${valor - (valor * 10 / 100):.2f} no final')
elif o == 2:
    print(f' sua de R${valor:.2f} vai custar R${valor - (valor * 5 / 100):.2f} no final')
elif o == 3:
    print(f'Sua compra será parcelada em 2x de R${valor / 2:.2f}')
elif o == 4:
    p = int(input('Quantas parcelas? '))
    t = valor + valor * 20 / 100
    print(f'Sua compra será parcelada em {p}x de R${t / p:.2f}')
    print(f'Sua compra de R${valor:.2f} vai custar R${t:.2f} no final')
else:
    print('Opção invalida!')
    print(f'Sua compra continuará custando R${valor:.2f}')
