from equacoes import equacoes_2_grau
from inequacoes import inequacoes_2_grau
from simplificador import simplificar_inequacao

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