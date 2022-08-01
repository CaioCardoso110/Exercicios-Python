n = str(input('Digite uma frase: ')).strip().lower()
print(f'A letra A aparece {n.count("a")} vezes\nA primeira letra A apareceu na posição {n.find("a")+1}\nA ultima letra A apareceu na posição {n.rfind("a")+1}')
