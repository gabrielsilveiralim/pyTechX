""" Menu de Operações Matemáticas
Exibe um menu com 4 operações e executa a operação escolhida
pelo usuário, usando match / case.
"""


def menu_operacoes():
    print("=== Menu de Operações ===")
    print("1 - Soma")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisão")
    opcao = int(input("Escolha uma opção: "))

    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))

    match opcao:
        case 1:
            print(f"Resultado: {num1 + num2}")
        case 2:
            print(f"Resultado: {num1 - num2}")
        case 3:
            print(f"Resultado: {num1 * num2}")
        case 4:
            if num2 != 0:
                print(f"Resultado: {num1 / num2}")
            else:
                print("Erro: divisão por zero")
        case _:
            print("Opção inválida")


if __name__ == "__main__":
    menu_operacoes()


"""
Portugol

programa
{
    funcao inicio()
    {
        inteiro opcao
        real num1, num2, resultado

        escreva("=== Menu de Operações ===")
        escreva("1 - Soma")
        escreva("2 - Subtração")
        escreva("3 - Multiplicação")
        escreva("4 - Divisão")
        escreva("Escolha uma opção: ")
        leia(opcao)

        escreva("Digite o primeiro número: ")
        leia(num1)
        escreva("Digite o segundo número: ")
        leia(num2)

        escolha(opcao)
        {
            caso 1:
                resultado = num1 + num2
                escreva("Resultado: ", resultado)
                pare
            caso 2:
                resultado = num1 - num2
                escreva("Resultado: ", resultado)
                pare
            caso 3:
                resultado = num1 * num2
                escreva("Resultado: ", resultado)
                pare
            caso 4:
                se (num2 != 0)
                {
                    resultado = num1 / num2
                    escreva("Resultado: ", resultado)
                }
                senao
                {
                    escreva("Erro: divisão por zero")
                }
                pare
            caso contrario:
                escreva("Opção inválida")
        }
    }
}
"""