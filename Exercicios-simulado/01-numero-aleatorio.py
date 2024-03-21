import random 

random_number = random.randint(1,100)

while True:
    n = int(input('Entre com um número, por favor: '))

    if random_number == n :
        print('Parabéns!')
        break
    elif random_number > n :
        print('Palpite está baixo')
    else :
        print('Palpite está alta')