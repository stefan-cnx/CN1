guessed_list = []

# Function that will pick a number sequence as one string
def pick_num_seq():
    # Starting of with one number sequence for testing
    return '1, 4 , 9, 16, 25'

def split_string(seq):
    split_string_of_sequence = list(seq)
    return split_string_of_sequence

def display_nums(chars, guessed_list):
   for i in range(len(chars)):
        correct_char = False
        for j in range(len(guessed_list)):
            if chars[i] == guessed_list[j]:
                correct_char = True
                break
        #print(correct_char)
        #print(chars[i])
        if correct_char == True and chars[i] != ' ':
            print(chars[i], end ='')
            #print('Will Print: ',chars[i] )
        elif chars[i] == ',':
            print(',', end =' ')
            #print('Will Print: ', ',')
        elif chars[i] == ' ':
            print('', end ='')
            #print('Will Print: ', 'nothing')
        else:
            print('_', end ='')
            #print('Will Print: ', '_')

def guess_char(guessed_list):
    new_guess = input('Guess a number between 0-9: ')
    guessed_list.append(new_guess)
    return guessed_list


seq = pick_num_seq()
chars = split_string(seq)
display_nums(chars, guessed_list)
for i in range(6):
    print('\nThis is your', str(i+1) + '. attempt:')
    guess_char(guessed_list)
    print('\n')
    display_nums(chars, guessed_list)
    print('\n')




