d = float(input('Qual a distancia da sua viagem? '))
print(f'Você está prestes a começar uma viagem de {d:.1f}Km')
if d <= 200:
    p = d * 0.50
    print(f'E o preço da sua passagem será R${p:.2f}')
else:
    p = d * 0.45
    print(f'E o preço da sua passagem será R${p:.2f}')
