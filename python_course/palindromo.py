def palindromo(word):# ejemplo del profe, en onenote tengo el mismo pero mas resumido LOOK
    word = word.replace(' ', ' ').lower()#esto es para eliminar los espacios y poner en lower, este es como un shortcut
    # word = word.lower()
    inverted_word = word[::-1]
    if word == inverted_word:
        return True
    else:
        return False
    


def run():# dejas dos espacios enter cada funcion y tambien en el entry point
    word = input('Type a word: ')
    is_palindromo = palindromo(word)
    if is_palindromo == True:
        print('it is palindromo')
    else:
        print('its not palindromo')


if __name__ == '__main__':# el entry point todo lo que este debajo se ejecuta,
    run()