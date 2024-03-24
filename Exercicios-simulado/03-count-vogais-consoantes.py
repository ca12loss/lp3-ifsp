def count_vowelsncons(phrase):
    count_vowel = 0
    count_consonant = 0

    for letter in phrase.replace(" ", "") :
        if letter.lower() in 'aeiou':
            count_vowel += 1
        else:
            count_consonant += 1
    return count_vowel, count_consonant

phrase = input('Entre com a frase, por favor: ')
vowel_count, consonant_count = count_vowelsncons(phrase)
print(f'Quantidade de vogais: {vowel_count}')
print(f'Quantidade de consoantes: {consonant_count}')

