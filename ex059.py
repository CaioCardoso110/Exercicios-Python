from time import sleep
n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
acabou = False
while not acabou:
    print('''    [ 1 ] somar
    [ 2 ] multiplicar
    [ 3 ] maior
    [ 4 ] novos números
    [ 5 ] sair do programa''')
    opção = int(input('>>>>> Qual é a sua opção? '))
    if opção == 1:
        print(f'A soma entre {n1} + {n2} é {n1+n2}')
        print('=-' * 15)
    elif opção == 2:
        print(f' O resultado de {n1} x {n2} é {n1 * n2}')
        print(f'-=' * 15)
    elif opção == 3:
        if n1 > n2:
            print(f'Entre {n1} e {n2} o maior valor é {n1}')
        elif n1 < n2:
            print(f'Entre {n1} e {n2} o maior valor é {n2}')
        else:
            print('Os dois valores são iguais')
        print('-=' * 15)
    elif opção == 4:
        print('Informe os numeros novamente: ')
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))
    elif opção == 5:
        acabou = True
        print('Finalizando...')
        sleep(3)
        print('-=' * 15)
        print('Fim do programa! Volte sempre!')
    else:
        print('Opção invalida. Tente novamente')
        print('-=' * 15)
