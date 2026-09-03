## Calculadora com dividir tratando divisão por zero

def dividir(a, b):
    try:
        resultado = a / b
        return resultado
    except ZeroDivisionError:
        return "Erro: Divisão por zero não permitida"

print(dividir(10, 2))  # Saída: 5.0
print(dividir(10, 0))  # Saída: Erro: Divisão por zero não permitida