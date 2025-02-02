import math
from sympy import symbols, expand, sympify

# Calculadora de Equações e Inequações de 2.º grau

print("Calculadora de equações e inequações do 2.º grau do tipo:\n\nax^2 + bx + c = 0 ou ax^2 + bx + c > 0\n")

def equacoes_2_grau():
    print("\nCálculo de Equações do 2.º grau")
    print("1.º Transforme para uma equação do tipo ax^2 + bx + c.\n2.º Indique os valores de a, b e c.\n")

    a = float(input("Indique um valor de a: "))
    b = float(input("Indique um valor de b: "))
    c = float(input("Indique um valor de c: "))

    delta = (b**2) - (4*a*c)

    if delta > 0:
        x_1 = (-b - math.sqrt(delta)) / (2 * a)
        x_2 = (-b + math.sqrt(delta)) / (2 * a)
        print(f"A equação tem 2 soluções reais: x = {x_1}, x = {x_2}")
    elif delta == 0:
        x_0 = -b / (2 * a)
        print(f"A equação tem 1 solução real: x = {x_0}")
    else:
        print(f"A equação não tem soluções reais, pois delta = {delta}.")