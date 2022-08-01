from math import radians, sin, cos, tan, ceil
n = float(input('Digite o ângulo que você deseja: '))
r = radians(n)
print(f'O ângulo de {n} tem o SENO de {sin(r):.2f}\nO ângulo de {n} tem o COSENO de {cos(r):.2f}\nO ângulo de {n} tem '
      f'a TANGENTE de {tan(r):.2f}')
