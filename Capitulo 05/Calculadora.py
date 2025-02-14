print("\n******************* Calculadora em Python Lab02 *******************")


# Definindo funções de operações
def soma(x, y):
    return x + y


def subtracao(x, y):
    return x - y


def multiplicacao(x, y):
    return x * y


# Aqui verifica se a divisão e diferente de zero, se for divisão por zero exibe msn, se não divide
def divisao(x, y):
    if y != 0:
        return x / y
    else:
        return "Erro: Divisão por zero!"


# Exibe opçãoes do menu
def calculadora():
    print("Selecione a operação:")
    print("1. Soma")
    print("2. Subtração")
    print("3. Multiplicação")
    print("4. Divisão")

    # pede que digite a operação que deseja realizar
    escolha = input("Digite sua escolha de 1 a 4: ")

    if escolha in ['1', '2', '3', '4']:
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))

        # Operação de Soma
        if escolha == '1':
            print(f"Resultado: {num1} + {num2} = {soma(num1, num2)}")
        # Operação de Subtração
        elif escolha == '2':
            print(f"Resultado: {num1} - {num2} = {subtracao(num1, num2)}")
        # Operação de Multiplicação
        elif escolha == '3':
            print(f"Resultado: {num1} * {num2} = {multiplicacao(num1, num2)}")
        # Operação de divisão
        elif escolha == '4':
            print(f"Resultado: {num1} / {num2} = {divisao(num1, num2)}")
    else:
        # se a escolha for diferente de alguma do menu retorna a msn de escolha invalida
        print("Escolha inválida. Por favor, selecione uma opção entre 1 e 4.")


# Executa a calculadora
calculadora()
