from random import shuffle

def scramble_word(word):
    print('This is the word that was passed into this function:', word)
    word = list(word)
    print('This is the list that was created from the list() function using the \'word\' that was passed into this function:', word)
    shuffle(word)
    print('This is the list after it was shuffled by the shuffle() function:', word)
    word = ''.join(word)
    print('This is the word after it was shuffled from the list and joined into one string with the join() function:', word)
    return word   
print(scramble_word('PASTA'))
