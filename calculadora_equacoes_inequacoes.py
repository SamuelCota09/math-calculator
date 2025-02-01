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

# Simplificador de inequações

def simplificar_inequacao():
    # Pedir input do utilizador
    inequacao_usuario = input("Insira a inequação (exemplo: 2*x^2 + 3*x - 5 <= 4*x^2 - x + 7): ")

    # Definir a variável simbólica
    x = symbols('x')
    
    # Dividir a inequação em lado esquerdo (lhs) e lado direito (rhs)
    lhs, rhs = inequacao_usuario.split("<=") if "<=" in inequacao_usuario else \
               inequacao_usuario.split(">=") if ">=" in inequacao_usuario else \
               inequacao_usuario.split("<") if "<" in inequacao_usuario else \
               inequacao_usuario.split(">")
    
    # Converter os lados para expressões simbólicas
    lhs_expr = sympify(lhs.strip())
    rhs_expr = sympify(rhs.strip())
    
    # Mover todos os termos para o lado esquerdo: lhs - rhs <= 0
    expr_final = lhs_expr - rhs_expr
    
    # Expandir a expressão final
    expr_final_expandida = expand(expr_final)
    
    # Determinar a desigualdade original
    if "<=" in inequacao_usuario:
        desigualdade = "<="
    elif ">=" in inequacao_usuario:
        desigualdade = ">="
    elif "<" in inequacao_usuario:
        desigualdade = "<"
    elif ">" in inequacao_usuario:
        desigualdade = ">"
    
    # Retornar a inequação simplificada
    print("Inequação simplificada:", f"{expr_final_expandida} {desigualdade} 0")

# Menu para escolher entre equações e inequações

while True:
    print("\nEscolha uma opção:")
    print("1. Resolver Equação do 2.º grau")
    print("2. Simplificador de Inequações do 2.º grau para a fórmula canónica")
    print("3. Resolver Inequação do 2.º grau")
    print("4. Sair")
    
    opcao = input("Opção: ").strip()
    if opcao == "1":
        equacoes_2_grau()
    elif opcao == "2":
        simplificar_inequacao()
    elif opcao == "3":
        inequacoes_2_grau()
    elif opcao == "4":
        print("Obrigado por usar a calculadora!")
        break
    else:
        print("Opção inválida. Tente novamente.")