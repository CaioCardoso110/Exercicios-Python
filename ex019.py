from random import choice
alunos = []
for contador in range(1, 5):
    alunos.append(str(input(f'Digite o nome do {contador}° aluno: ')))
print(f'O aluno escolhido foi {choice(alunos)}')
