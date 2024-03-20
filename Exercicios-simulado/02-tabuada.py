n = int(input('Entre com o número que deseja conferir a tabuada: '))

for count in range(0,10,1):
    print(f'{n} x {count + 1} = {n*(count+1)}')
