from random import shuffle
alunos = []
for contador in range(1, 5):
    alunos.append(str(input(f'\33[1;30;41m{contador}° Aluno:\33[m ')))
shuffle(alunos)
print(f'\33[1;33;44mA ordem de apresentação será:\33[m \33[0;32m{alunos}\33[m')
