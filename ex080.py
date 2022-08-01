lista = []
for contador in range(0, 5):
    numero = int(input('Digite um valor: '))
    if contador == 0 or numero > lista[-1]:
        lista.append(numero)
        print('Valor adicionado na ultima posição')
    else:
        posicao = 0
        while posicao < len(lista):
            if numero < lista[posicao]:
                lista.insert(posicao, numero)
                print(f'Adicionado a posição {posicao}')
                break
            posicao += 1
print(f'Os valores digitados em ordem foram {lista}')
