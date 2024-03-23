
print('Jogo da Forca: ')

secret_word = 'sometimes'
chances = 6

to_reveal = ['_'] * len(secret_word)

while chances > 0:

    letter = input('\nAdivinhe uma letra : ')
    found = False

    for i in range(len(secret_word)):
        if letter == secret_word[i]:
            to_reveal[i] = letter
            found = True

    if not found:
        print('Esta letra não pertence a esta palavra') 
        chances -=1
        print(f'Ainda possui {chances} tentativas')

    print(''.join(to_reveal))

    if '_' not in to_reveal:
        print("Parabéns! Você acertou a palavra!")
        break

if '_' in to_reveal:
    print("Você perdeu! A palavra era:", secret_word)
