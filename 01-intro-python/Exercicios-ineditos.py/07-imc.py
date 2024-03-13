weight = float(input("Entre com o seu peso, por favor: "))
height = float(input("Entre com a sua altura em metros, por favor: "))

def calculate_imc(weight,height):
    return weight/height**2

imc = calculate_imc(weight,height)
print = (imc)