phrase = input('Entre com a frase, por favor: ')

count_vowel = 0
count_consonant = 0


for i in range(0,len(phrase),1):
    if  phrase[i] == 'a' or phrase[i] == 'e' or phrase[i] == 'i' or phrase[i] == 'o' or phrase[i] == 'u' :
        count_vowel+=1
    else:
        count_consonant+=1

print(f'Quantidade de vogais:{count_vowel}')
print(f'Quantidade de consoantes:{count_consonant}')
