from random import randrange

# DEFINE pick_random_word():
def pick_random_word(words_list):
    print('This is the list of words that were passed into this function:\n', words_list)
    print('There are', len(words_list), 'elements in our list')
    random_index = randrange(len(words_list))
    print('This is a random number that we could use as index:', random_index)
    print('This is the word that will be returned with the random index:', words_list[random_index])
    return words_list[random_index]

words_list = ['APPLE', 'PAPER', 'BANANA', 'FOAM', 'CAT']

random_word = pick_random_word(words_list)
print(random_word)
words_list.remove(random_word)

random_word = pick_random_word(words_list)
print(random_word)
words_list.remove(random_word)

random_word = pick_random_word(words_list)
print(random_word)
words_list.remove(random_word)

random_word = pick_random_word(words_list)
print(random_word)
words_list.remove(random_word)

random_word = pick_random_word(words_list)
print(random_word)
words_list.remove(random_word)

#no words left, this should print an empty list
print(words_list)

"""
THIS IS A SAMPLE OUTPUT OF ABOVE SCRIPT:
========================================
This is the list of words that were passed into this function:
 ['APPLE', 'PAPER', 'BANANA', 'FOAM', 'CAT']
There are 5 elements in our list
This is a random number that we could use as index: 3
This is the word that will be returned with the random index: FOAM
FOAM
This is the list of words that were passed into this function:
 ['APPLE', 'PAPER', 'BANANA', 'CAT']
There are 4 elements in our list
This is a random number that we could use as index: 2
This is the word that will be returned with the random index: BANANA
BANANA
This is the list of words that were passed into this function:
 ['APPLE', 'PAPER', 'CAT']
There are 3 elements in our list
This is a random number that we could use as index: 1
This is the word that will be returned with the random index: PAPER
PAPER
This is the list of words that were passed into this function:
 ['APPLE', 'CAT']
There are 2 elements in our list
This is a random number that we could use as index: 1
This is the word that will be returned with the random index: CAT
CAT
This is the list of words that were passed into this function:
 ['APPLE']
There are 1 elements in our list
This is a random number that we could use as index: 0
This is the word that will be returned with the random index: APPLE
APPLE
[]
"""
