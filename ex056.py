totidade = 0
velidade = 0
velho = ''
mulhernova = 0
for c in range(1, 5):
    print('='*5, f'{c}° PESSOA', '='*5)
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).upper().strip()
    totidade += idade
    if c == 1 and sexo == 'M':
        velidade = idade
        velho = nome
    else:
        if idade > velidade:
            velidade = idade
            velho = nome
    if sexo == 'F' and idade < 20:
        mulhernova += 1
print(f'A idade média do grupo é de {totidade / 4} anos.')
print(f'O homem mais velho tem {velidade} anos e se chama {velho}.')
print(f'Ao todo são {mulhernova} mulheres com menos de 20 anos')
