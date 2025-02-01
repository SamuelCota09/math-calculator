import math
from sympy import symbols, expand, sympify

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
