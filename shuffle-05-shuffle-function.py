from random import shuffle
from random import randrange

# DEFINE pick_random_word():
def pick_random_word(words_list):
    random_index = randrange(len(words_list))
    return words_list[random_index]


#scramble_word():
def scramble_word(word):
    word = list(word)
    shuffle(word)
    return ''.join(word)


# START Guess the Shuffled Word:
# SET 'words_list' to a list of words
words_list = ['APPLE', 'PAPER', 'BANANA', 'FOAM', 'CAT']
# SET 'word' from CALL pick_random_word() from 'words_list'
word = pick_random_word(words_list)
# SET 'scrambled' by scrambling 'word'
scrambled = scramble_word(word)
# OUTPUT 'scrambled'
print(scrambled)
# WHILE guessed word is incorrect:
guess = ''
while word != guess:
#   SET 'guess' to INPUT from asking user to guess the word
    guess = input('Guess the word: ')
#   IF 'guess' matches 'word', e.g. user guessed the correct word:
    if guess == word:
#       OUTPUT the message that the guessed word is correct
        print('You guessed the correct word. Congratulations!')
#       Break out of the while loop
        break
#   ELSE
    else:
#       OUTPUT the message that guessed word is incorrect and try again
        print('You didn\'t guess the correct word. Try again!')
# END Guess the Shuffled Word
