""" Script Principal
Importa os módulos criados (calculadora, utilidades, lista_segura)
e demonstra o reaproveitamento de código.
"""

from modulos import calculadora, utilidades
from lista_segura import adicionar_item_seguro


def main():
    print("=== Demonstração do módulo calculadora ===")
    print("Soma:", calculadora.somar(10, 5))
    print("Subtração:", calculadora.subtrair(10, 5))
    print("Multiplicação:", calculadora.multiplicar(10, 5))
    print("Divisão por zero:", calculadora.dividir(10, 0))
    print("Divisão normal:", calculadora.dividir(10, 2))

    print("\n=== Demonstração do módulo utilidades ===")
    print("32°C em Fahrenheit:", utilidades.converter_temperatura(32, "C"))
    valida, msg = utilidades.validar_senha("Senha@123")
    print("Validação de senha:", msg)
    print("Total da caixa:", utilidades.caixa(10.5, 25.0, 7.3))
    print(utilidades.ficha_aluno(nome="Gabriel", idade=22, curso="ADS"))

    print("=== Demonstração de lista segura ===")
    lista_original = [1, 2, 3]
    nova_lista = adicionar_item_seguro(lista_original, 4)
    print("Lista original (inalterada):", lista_original)
    print("Nova lista:", nova_lista)


if __name__ == "__main__":
    main()

    