#Calculadora de troco - Recebe o valor da compra e o valor pago, calcula e imprime o troco.

calculator = float(input("Digite o valor da compra: "))
paid = float(input("Digite o valor pago: "))

troco = paid - calculator
print(f"O troco é: R$ {troco:.2f}")