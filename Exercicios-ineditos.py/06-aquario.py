
def find_volume(lenght,height,width):
    return (lenght*height*width)/1000

def get_potency(volume,desired_temperature,ambient_temperature):
    return volume*0.05*(desired_temperature - ambient_temperature)
 

def get_hrly_filter(volume):
    return volume*2, volume*3

lenght = float(input("Entre com o comprimento, por favor: "))
height = float(input("Entre com a altura, por favor: "))
width = float(input("Entre com a largura, por favor: "))
des_temp = float(input("Entre com a temperatura desejada, por favor: "))
amb_temp = float(input("Entre com a temperatura ambiente, por favor: "))

volume = find_volume(lenght, height, width)
potency = get_potency(volume,des_temp,amb_temp)
filter_min, filter_max = get_hrly_filter(volume)

print(f"\nO volume do aquário é: {volume}L\nA potencia é: {potency} watts")
print(f"A filtragem por hora mínima é: {filter_min}L e a filtragem máxima é : {filter_max}L")



