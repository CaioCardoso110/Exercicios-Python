n = str(input('Digite seu nome completo: ')).strip().title()
n1 = n.split()
print("Muito prazer em te conhecer!")
print(f'Seu primeiro nome é {n1[0]}\nSeu ultimo nome é {n1[len(n1)-1]}')
