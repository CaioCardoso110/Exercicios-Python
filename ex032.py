from datetime import datetime
ano = int(input('Que ano quer analisar? Digite 0 se for o ano atual: '))
if ano == 0:
    ano = datetime.today().year
if ano % 100 != 0 and ano % 4 == 0 or ano % 400 == 0:
    print(f'O ano é {ano} é bissexto!')
else:
    print(f'O ano {ano} não é bissexto!')
