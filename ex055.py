pesado = 0
leve = 1000
for c in range(1, 6):
    peso = float(input(f'Peso da {c}° pessoa: '))
    if c == 1:
        pesado = peso
        leve = peso
    else:
        if peso > pesado:
            pesado = peso
        if peso < leve:
            leve = peso
print(f'O maior peso lido foi de {pesado}kg')
print(f'O menor peso lido foi de {leve}kg')
