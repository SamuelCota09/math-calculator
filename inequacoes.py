import math

def inequacoes_2_grau():
    print("\nCálculo de Inequações do 2.º grau")
    print("1.º Transforme para uma inequação do tipo ax^2 + bx + c > 0 ou ax^2 + bx + c < 0.")
    print("2.º Indique os valores de a, b e c.\n")

    a = float(input("Indique um valor de a: "))
    b = float(input("Indique um valor de b: "))
    c = float(input("Indique um valor de c: "))

    delta = (b**2) - (4*a*c)

    if delta > 0:
        x_1 = (-b - math.sqrt(delta)) / (2 * a)
        x_2 = (-b + math.sqrt(delta)) / (2 * a)
        print(f"A inequação tem as raízes: x1 = {x_1}, x2 = {x_2}")

        # Intervalos dependem do sinal de 'a'
        if a > 0:
            print(f"A solução para ax^2 + bx + c > 0 é: ]-∞, {x_1}[ U ]{x_2}, +∞[")
            print(f"A solução para ax^2 + bx + c < 0 é: ]{x_1}, {x_2}[")
        else:
            print(f"A solução para ax^2 + bx + c > 0 é: ]{x_1}, {x_2}[")
            print(f"A solução para ax^2 + bx + c < 0 é: ]-∞, {x_1}[ U ]{x_2}, +∞[")

    elif delta == 0:
        x_0 = -b / (2 * a)
        if a > 0:
            print(f"A solução para ax^2 + bx + c > 0 é: ]-∞, {x_0}[ U ]{x_0}, +∞[")
            print(f"A solução para ax^2 + bx + c < 0 é: vazio (∅)")
        else:
            print(f"A solução para ax^2 + bx + c > 0 é: vazio (∅)")
            print(f"A solução para ax^2 + bx + c < 0 é: ]-∞, {x_0}[ U ]{x_0}, +∞[")
    else:
        if a > 0:
            print("Como delta < 0 e a > 0, a solução para ax^2 + bx + c > 0 é: ]-∞, +∞[")
            print("A solução para ax^2 + bx + c < 0 é: vazio (∅)")
        else:
            print("Como delta < 0 e a < 0, a solução para ax^2 + bx + c < 0 é: ]-∞, +∞[")
            print("A solução para ax^2 + bx + c > 0 é: vazio (∅)")
    print("Ajuste a solução conforme seja <, >, <=, >=.")