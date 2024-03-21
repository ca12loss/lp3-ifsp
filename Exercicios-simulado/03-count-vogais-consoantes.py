def count_vowelsncons(phrase):
    phrase1 = phrase.replace(" ", "")
    count_vowel = 0
    count_consonant = 0

    for i in range(0, len(phrase1), 1):
        if phrase1[i] == 'a' or phrase1[i] == 'e' or phrase1[i] == 'i' or phrase1[i] == 'o' or phrase1[i] == 'u':
            count_vowel += 1
        else:
            count_consonant += 1
    return count_vowel, count_consonant

phrase = input('Entre com a frase, por favor: ')
vowel_count, consonant_count = count_vowelsncons(phrase)
print(f'Quantidade de vogais: {vowel_count}')
print(f'Quantidade de consoantes: {consonant_count}')

