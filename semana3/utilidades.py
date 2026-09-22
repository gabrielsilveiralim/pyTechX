"""
Módulo utilidades
Contém: conversor de temperatura, validador de senha,
caixa com *precos e ficha do aluno com **dados.
"""


def converter_temperatura(valor, unidade_origem):
    """Converte temperatura entre Celsius e Fahrenheit.
    unidade_origem: 'C' (converte para Fahrenheit) ou 'F' (converte para Celsius).
    """
    unidade_origem = unidade_origem.upper()
    if unidade_origem == "C":
        return valor * 9 / 5 + 32
    elif unidade_origem == "F":
        return (valor - 32) * 5 / 9
    else:
        raise ValueError("Unidade inválida. Use 'C' ou 'F'.")


def validar_senha(senha):
    """Valida se a senha tem no mínimo 8 caracteres, uma letra maiúscula,
    uma minúscula, um número e um caractere especial.
    Retorna uma tupla (bool, mensagem)."""
    if len(senha) < 8:
        return False, "A senha deve ter no mínimo 8 caracteres."
    if not any(c.isupper() for c in senha):
        return False, "A senha deve ter ao menos uma letra maiúscula."
    if not any(c.islower() for c in senha):
        return False, "A senha deve ter ao menos uma letra minúscula."
    if not any(c.isdigit() for c in senha):
        return False, "A senha deve ter ao menos um número."
    caracteres_especiais = "!@#$%^&*()-_=+"
    if not any(c in caracteres_especiais for c in senha):
        return False, "A senha deve ter ao menos um caractere especial."
    return True, "Senha válida."


def caixa(*precos):
    """Recebe uma quantidade variável de preços (*args) e retorna o total."""
    return sum(precos)


def ficha_aluno(**dados):
    """Recebe dados variáveis do aluno (**kwargs) e monta uma ficha em texto."""
    ficha = "=== Ficha do Aluno ===\n"
    for chave, valor in dados.items():
        ficha += f"{chave.capitalize()}: {valor}\n"
    return ficha