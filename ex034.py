salario = int(input('Qual é o salario do funcionario? R$'))
if salario < 1250:
    aumento = salario + (salario * 15 / 100)
else:
    aumento = salario + (salario * 10 / 100)
print(f'Quem ganhava R${salario:.2f} passa a ganhar R${aumento:.2f}')