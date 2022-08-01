from datetime import datetime
maior = 0
menor = 0
atual = datetime.today().year
for c in range(1, 8):
    ano = int(input(f'Em que ano a {c}° pessoa nasceu? '))
    if atual - ano >= 18:
        maior += 1
    else:
        menor += 1
print(f'Ao todo tivemos {maior} pessoas maiores de idade')
print(f'E tambem tivemos {menor} pessoas menores de idade')
