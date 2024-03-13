purchased_value = float(input('Entre com o valor da compra, por favor: '))

if purchased_value > 0.0 and purchased_value < 9.99 :
    discount = purchased_value * 0
elif purchased_value > 10.0 and purchased_value < 99.0 :
    discount = purchased_value * 0.05
elif purchased_value > 100 and purchased_value < 499.99 :
    discount = purchased_value * 0.1
else :
    discount = purchased_value * 0.15

print("Valor da compra é: ", purchased_value - discount)