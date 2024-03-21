word = input('Entre com a palavra: ')
inverted_word = ''

for i in range(len(word)-1, -1, -1):
    inverted_word += word[i]

if inverted_word == word:
    print('A palavra é palíndromo')
else:
    print('A palavra não é palindromo')    

