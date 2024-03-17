def calculate_imc(weight,height):
    return weight/height**2

def getto_normalweight(weight,height):
    normal = 24.9

    if imc < 18.5:
        return ((height**2)*18.5)-weight
    else:
        return weight-((height**2)*normal)


weight = float(input("Entre com o seu peso, por favor: "))
height = float(input("Entre com a sua altura em metros, por favor: "))

imc = round(calculate_imc(weight,height),2)
getto_normal = round(getto_normalweight(weight,height),2)

under = imc<18.5
normal = imc>=18.5 and imc<=24.9
over = imc>=25 and imc<=29.9
obesity1 = imc<=30 and imc<=34.9
obesity2 = imc<=35 and imc<=39.9
obesity3 = imc>=40

print(f"O seu imc é: {imc}")

if under :
    print(f"Você está {getto_normal} Kg abaixo do peso")
elif normal :
    print("Peso normal")
elif over :  
    print(f"Você está {getto_normal} sobrepeso")
elif obesity1 :
    print(f"Obesidade 1. Precisa perder:{getto_normal} Kg.")
elif obesity2 :
    print(f"Obesidade 2. Precisa perder:{getto_normal} Kg.")
else :
    print(f"Obesidade 3. Precisa perder:{getto_normal} Kg.")

