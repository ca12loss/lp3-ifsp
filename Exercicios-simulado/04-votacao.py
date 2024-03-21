print('Vote em um dos 3 candidatos, por favor: ')
print('Digite as opções correspondentes: ')

while True:
    print('1-Candidato 1\n2-Candidato 2\n3-Candidato 3')
    n = int(input())

    c1 = 0
    c2 = 0
    c3 = 0

    if n == 1:
        c1+=1
    elif n == 2:
        c2+=1
    else:
        c3+=1
    
    print('Deseja continuar a votação? Digite: ')
    keeping_voting = int(input('1-Sim ou 2-Conferir resultados\n'))

    if keeping_voting != 1:
        break

votes = [c1,c2,c3]
max_votes = max(votes)

if c1 == max_votes:
    print('O candidato ganhador foi: Candidato 1')
elif c2 == max_votes:
    print('O candidato ganhador foi: Candidato 2')
else:
    print('O candidato ganhador foi: Candidato 3')

    

