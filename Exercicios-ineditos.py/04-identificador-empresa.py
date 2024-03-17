def verify_id(employee_id) :

    valid_lenght = len(employee_id) == 7 
    valid_start_end = employee_id.startswith("BR") and employee_id.endswith("X") 
    valid_middle = employee_id[2] != '0' and employee_id[3] != '0' and employee_id[4] != '0' and employee_id[5] !='0'

    valid_id = valid_lenght and valid_start_end and valid_middle

    if valid_id:
       return "Código válido!"
    else:
       return "Código inválido!"

employee_id = input("Entre com o seu identificador, por favor: ")

validation = verify_id(employee_id)
print(validation)



