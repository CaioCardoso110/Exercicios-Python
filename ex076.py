lista = ('Lápis', 1.75,
        'Borracha', 2.00,
         'Caneta', 1.20,
          'Caderno', 7.50,
           'Lapiseira', 1.99)
print('=' * 30)
print(f'{"Lista de Compra":^30}')
print('=' * 30)
for item in range(0, len(lista)):
    if item % 2 == 0:
        print(f'{lista[item]:.<30}', 'R$', end='')
    else:
        print(f'{lista[item]:>7.2f}')

