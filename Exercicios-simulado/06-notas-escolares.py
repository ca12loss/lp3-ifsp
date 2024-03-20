def convert_grades(grade):

    if grade < 60 :
        return 'F'
    elif grade >= 60 and grade < 70: 
        return 'D'
    elif grade >= 70 and grade < 80:
        return'C' 
    elif grade >= 80 and grade < 90:
        return'B'
    else: 
        return 'A' 
    
grade = int(input("Entre com a nota de 0 até 100, por favor: "))
print(f'A nota é:{convert_grades(grade)}')

