print('-' * 30)
print('CADASTRE UMA PESSOA')
print('-' * 30)
maioridade = 0
homens = 0
menoridadef = 0
while True:
    idade = int(input('Idade: '))
    sexo = str(input('Sexo: [M/F] ')).strip().lower()[0]
    print('-' * 30)
    if sexo != 'f' and sexo != 'm':
        sexo = str(input('Termo invalido, tente novamente. Sexo: [M/F] ')).strip().lower()[0]
    if idade >= 18:
        maioridade += 1
    if sexo == 'm':
        homens += 1
    if sexo == 'f' and idade < 20:
        menoridadef += 1
    r = ' '
    while r not in 'sn':
        r = str(input('Quer Continuar? [S/N] ')).strip().lower()[0]
    if r == 'n':
        break
print(f'Total de pessoas com mais de 18 anos: {maioridade}')
print(f'Ao todo temos {homens} homens cadastrados')
print(f'E temos {menoridadef} mulheres com menos de 20 anos')
