# Par ou impar - recebe um número inteiro e informa se ele é par ou ímpar

number= int(input("Digite um número inteiro: "))

if number % 2 == 0:
    print(f"{number} é um número par")
else:
    print(f"{number} é um número ímpar")   