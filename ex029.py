v = float(input('Qual a velocidade atual do carro? '))
if v > 80:
    m = (v - 80) * 7
    print(f'Multado! Você excedeu o limite permitido de 80Km/h\nDeve pagar uma multa de R${m:.2f}!')
print("Tenha um bom dia! Dirija com segurança!")