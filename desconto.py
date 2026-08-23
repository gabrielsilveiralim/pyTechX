# Discount Calculator - receives price and discount (import math) = prints the final value of the product

price = float(input("Digite o preço do produto: "))
typeDescont = input("Digite 'p' para desconto em porcentagem ou 'v' para desconto em valor: ")

if typeDescont == 'p':
    discountPorcent = float(input("Digite o valor do desconto em porcentagem: "))
    end_price = price - (price * discountPorcent / 100)
elif typeDescont == 'v':
    discountPrice = float(input("Digite o valor do desconto em valor: "))
    end_price = price - discountPrice
else:
    print("Tipo de desconto inválido. Por favor, digite 'p' para porcentagem ou 'v' para valor.")

print("O valor final do produto com desconto é: R$ {:.2f}".format(end_price))