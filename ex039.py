from datetime import datetime
sexo = str(input('Qual o seu sexo para alistamento obrigatorio? M ou F: ')).upper()
if sexo == 'M':
    ano = int(input('Ano de nascimento: '))
    atual = datetime.today().year
    idade = atual - ano
    alis = 18 - idade
    print(f'Quem nasceu em {ano} tem {idade} anos em {atual}')
    if idade <= 17:
        print(f'Ainda faltam {alis} ano(s) para o seu alistamento')
        print(f'Seu alistamento será em {alis + atual}')
    elif idade > 18:
        print(f'Você ja deveria ter se alistado há {(atual - alis) - atual} anos')
        print(f'Seu alistamento foi em {atual + alis}')
    else:
        print('Você tem que se alistar imediatamente!')
elif sexo == 'F':
    print('Você não é obrigada a se alistar!')
else:
    print('Invalido. Tente novamente.')
