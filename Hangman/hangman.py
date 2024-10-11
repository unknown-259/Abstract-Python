# assignment: programming assignment 1
# author: Nathan Tran
# date: 04/12/23
# file: hangman.py is a program that allows the user to guess the word with a restricted number of lives.
# input: dictionary.txt, user input from the keyboard
# output: prompts in the terminal telling the user information based on their previous input

from random import choice, random

dictionary_file = "dictionary.txt"

# reads the file and updates the dictionary based on the size of each word.
# list for values
def import_dictionary(dictionary_file):
    dictionary = {}
    max_size = 12
    with open(dictionary_file) as dict:
        for i in dict:
            i = i.strip("\n")
            if len(i) not in dictionary:
                if len(i) <= 12:
                    dictionary.update({len(i): [i]})
                else:
                    dictionary.update({12: [i]})
            else:
                if len(i)-1 <= 12:
                    dictionary[len(i)].append(i)
                else:
                    dictionary[12].append(i)
    return dictionary

# get options size and lives from the user, use try-except statements for wrong input
def get_game_options() :  
    try:   
        size = int(input("\nPlease choose a size of a word to be guessed [3 - 12, default any size]:\n"))
        if size >= 3 and size <= 12:
            print(f"\nThe word size is set to {size}.")
        else:
            print("\nA dictionary word of any size will be chosen.")
            size = choice(list(dictionary.keys()))
    except:
        print("\nA dictionary word of any size will be chosen.")
        size = choice(list(dictionary.keys()))

    try:
        lives = int(input("\nPlease choose a number of lives [1 - 10, default 5]:\n"))
        if lives >= 1 and lives <=10:
            print(f"\nYou have {lives} lives.")
        else:
            lives = 5
            print(f"\nYou have {lives} lives.")
    except:
        lives = 5
        print(f"\nYou have {lives} lives.")
    return (size, lives)


if __name__ == '__main__' :

    # make a dictionary from a dictionary file
    dictionary = import_dictionary(dictionary_file)

    # print a game introduction
    print("Welcome to the Hangman Game!")

    # START MAIN LOOP (OUTER PROGRAM LOOP)
    cont = "Y"
    letters_chosen = []
    hidden_word = []
    word = ""
    while cont == "Y":

    # set up game options (the word size and number of lives)
        size, lives = get_game_options()
        word = choice(dictionary[size]).upper()
        letters_chosen = []
        lives_copy = lives
        bool = True
    
        # START GAME LOOP   (INNER PROGRAM LOOP)
        while lives_copy > 0:
            print(f"\nLetters chosen: {', '.join(letters_chosen)}\n")
            if len(hidden_word) < size:
                for i in range(size):
                    hidden_word.append("__")
                if "-" in word:
                    hidden_word[word.find("-")] = "-"
            print("  ".join(hidden_word), end = ' ')
            print(f"  lives: {lives_copy}", end = ' ')
            for i in range(lives-lives_copy):
                print("X", end = '')
            for j in range(lives_copy):
                print("O", end = '')

            letter = input("\n\nPlease choose a new letter >\n").upper()

            while letter.isalpha() == False or len(letter) >1:
                letter = input("\nPlease choose a new letter >\n").upper()

            if letter in letters_chosen: 
                bool = False

            while bool == False:
                print("\nYou have already chosen this letter.\n")
                letter = input("Please choose a new letter >\n").upper() 
                if letter not in letters_chosen:
                    bool = True
            letters_chosen.append(letter)
            if letter in word:
                print("\nYou guessed right!")
                index = [ind for ind in range(len(word)) if word.startswith(letter, ind)]
                for i in range(len(index)):
                    hidden_word[index[i]]= letter
            else:
                lives_copy -= 1
                print("You guessed wrong, you lost one life.")
            
            if "__" not in hidden_word:
                print(f"\nLetters chosen: {', '.join(letters_chosen)}\n")
                if len(hidden_word) < size:
                    for i in range(size):
                        hidden_word.append("__")
                    if "-" in word:
                        hidden_word[word.find("-")] = "-"
                print("  ".join(hidden_word), end = ' ')
                print(f"  lives: {lives_copy}", end = ' ')
                for i in range(lives-lives_copy):
                    print("X", end = '')
                for j in range(lives_copy):
                    print("O", end = '')
                break
        
        if lives_copy == 0:
            print(f"\nLetters chosen: {', '.join(letters_chosen)}\n")
            if len(hidden_word) < size:
                for i in range(size):
                    hidden_word.append("__")
                if "-" in word:
                    hidden_word[word.find("-")] = "-"
            print("  ".join(hidden_word), end = ' ')
            print(f"  lives: {lives_copy}", end = ' ')
            for i in range(lives-lives_copy):
                print("X", end = '')
            for j in range(lives_copy):
                print("O", end = '')
            print(f"\nYou lost! The word is {word}!")
            letters_chosen = []
            hidden_word = []
            cont = input("\nWould you like to play again [Y/N]?\n").upper()
        elif lives_copy > 0:
            print(f"\nCongratulations!!! You won! The word is {word}!")
            letters_chosen = []
            hidden_word = []
            cont = input("\nWould you like to play again [Y/N]?\n").upper()
        else:
            letters_chosen = []
            hidden_word = []
            cont = input("\nWould you like to play again [Y/N]?\n").upper()
    # Prints goodbye when exits the outer while-loop
    print("\nGoodbye!")