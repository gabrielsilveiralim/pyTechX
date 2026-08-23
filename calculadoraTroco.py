# Change Calculator - receives purchase amount and amount paid, calculates change

calculator = float(input("Digite o valor da compra: "))
paid = float(input("Digite o valor pago: "))

troco = paid - calculator
print(f"O troco é: R$ {troco:.2f}")