kg = int(input('Qual é o seu peso? (Kg) '))
m = float(input('Qual é a sua altura? (m) '))
imc = kg / (m ** 2)
print(f'O IMC desta pessoa é {imc:.1f}')
if imc < 18.5:
    print('Você está ABAIXO DO PESO normal')
elif imc < 25:
    print('PARABENS, você está na faixa de PESO NORMAL!')
elif imc < 30:
    print('Você está com SOBREPESO, cuidado!')
elif imc < 40:
    print('Você esta com OBESIDADE, cuidado!')
else:
    print('Você está em OBESIDADE MORBIDA, cuidado!')
