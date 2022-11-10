import random

words_list = ['python', 'java', 'javascript', 'php']

print("HANGMAN")
print("The game will be available soon")


def hangman():
    the_word = random.choice(words_list)
    list_word = []
    len_word = len(the_word)
    while len_word > 0:
        list_word.append('-')
        len_word -= 1

    hint = str(''.join(list_word))

    used_letters = set()
    num_try = 8
    print(hint)
    while num_try != 0:
        answer = input('name your letter:>')
        if answer.isupper() is True :
            print('Please, enter lowercase English letter')
        elif len(answer) != 1:
            print('You should input one letter')
        elif answer in used_letters:
            print('You have already guessed this letter before')
        elif answer not in used_letters :
            iteration_number = 0
            if answer in the_word:
                for n in the_word:
                    if iteration_number < len(the_word):
                        if answer == n:
                            list_word[iteration_number] = n
                        iteration_number += 1
            else:
                print('That letter does not appear in that word')
                num_try -= 1
        used_letters.add(answer)
        print((''.join(list_word)))
        if '-' not in list_word :
            print("You've guessed the word! Congrats!")
            break
    if num_try == 0:
        print('you have lost!')
    print('Thanks for playing! \n See ya next time!')


start_messege = input('Type "play" to play the game, tape "exit" to quit \n')
if start_messege == 'exit':
    print('See ya next time!')
elif start_messege == 'play':
    while start_messege == 'play':
        hangman()
        start_messege = input('Type "play" to play the game, tape "exit" to quit \n')
        if start_messege == 'exit':
            print('See ya next time!')
