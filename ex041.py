from datetime import datetime
ano = int(input('Ano de nascimento: '))
atual = datetime.today().year
idade = atual - ano
print(f'O atleta tem {idade} anos')
if idade <= 9:
    print('Classificação : MIRIM')
elif idade < 14:
    print('Classificação: INFANTIL')
elif idade < 19:
    print('Classificação: JÚNIOR')
elif idade < 25:
    print('Classificação: SÊNIOR')
else:
    print('Classificação: MASTER')