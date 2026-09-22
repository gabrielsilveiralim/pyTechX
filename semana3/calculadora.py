""" Módulo calculadora
Funções matemáticas básicas: somar, subtrair, multiplicar e dividir.
A função dividir trata explicitamente a divisão por zero.
"""


def somar(a, b):
    return a + b

def subtrair(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    """Divide a por b. Retorna None se b for zero, evitando
    que o programa quebre com ZeroDivisionError."""
    if b == 0:
        print("Erro: divisão por zero não é permitida.")
        return None
    return a / b


