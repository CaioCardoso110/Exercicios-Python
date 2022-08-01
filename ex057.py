sexo = str(input('Informe seu sexo: [M/F] ')).strip().upper()
while sexo != 'M' and sexo != 'F':
    sexo = str(input('Dados invalidos. Por favor, informe seu sexo: ')).upper()
print(f'Sexo {sexo} registrado com sucesso!')
