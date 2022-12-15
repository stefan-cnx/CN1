from random import shuffle

#scramble_word():
def scramble_word(orig_word):
    char_list = list(orig_word)
    shuffle(char_list)
    while ''.join(char_list) == orig_word:
        shuffle(char_list)
    return ''.join(char_list)

"""
# Test function below will output AOK or the word that is not on the expected outcome list
for i in range(10000):
    word = scramble_word('AND')
    if word == 'DNA' or word == 'DAN' or word == 'NAD' or word == 'NDA' or word == 'ADN':
        print('AOK')
    else:
        print('At', i, 'iteration the word', word, 'was returned.')
"""

for i in range(10000):
    word = scramble_word('AND')
    if not (word == 'DNA' or word == 'DAN' or word == 'NAD' or word == 'NDA' or word == 'ADN'):
        print('At', i, 'iteration the word', word, 'was returned.')

