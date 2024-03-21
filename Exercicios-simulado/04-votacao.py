print('Vote em um dos 3 candidatos, por favor: ')
print('Digite as opções correspondentes: ')

votes = [0,0,0]

while True:
    print('1-Candidato 1\n2-Candidato 2\n3-Candidato 3')
    n = int(input())

    if n == 1:
        votes[0]+=1
    elif n == 2:
        votes[1]+=2
    else:
        votes[2]+=3
    
    print('Deseja continuar a votação? Digite: ')
    keeping_voting = int(input('1-Sim ou 2-Conferir resultados\n'))

    if keeping_voting != 1:
        break

max_votes = max(votes)

for i in range(len(votes)):
    print(f'O Candidato {i+1} recebeu {votes[i]} votos.')

for i in range(len(votes)):
        if votes[i] == max_votes:
            print(f'\nO candidato ganhador foi: Candidato {i+1}')
            break
