import random 

n = int(input('Entre com um número, por favor: '))

random_number = random.randint(1,100)

if random_number == n:
    print('Acertou!') 
else :
    print('Errou!')

if random_number > n:
    diff = random_number - n
else :
    diff = n - random_number

if diff > 15 :
    print('Está frio!')
else :
    print('Está quente!')

print('Deseja continuar?/n1-Sim   2-Não')
