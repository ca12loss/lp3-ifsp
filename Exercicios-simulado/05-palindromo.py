def find_palin(phrase):
    phrase = phrase.lower().replace(" ","")
    rvrsd = phrase[::-1]
    return phrase == rvrsd

phrase = input('Entre com a frase: ')
print('É palíndromo') if find_palin(phrase) else print('Não é palíndromo')