# ---Final Game---
"""This function groups together all the sub-functions the create the game.
   The function also receives from the user a txt path and an integer."""


def Hangman():
    print_title()
    secret_word = user_input()
    print("Let's start!")
    num_of_tries = 1
    Max_Tries = 7
    print_hangman(num_of_tries)
    print('Secret-Word:  ' + '_ ' * len(secret_word),
          "(The length of the secret word is: {len})".format(len=len(secret_word)))
    old_letters_guessed = []
    while num_of_tries < Max_Tries:
        if check_win(secret_word, old_letters_guessed):
            break
        new_letter = input("Guess a letter: ")
        if try_update_letter_guessed(new_letter, old_letters_guessed):
            if new_letter in secret_word:
                print(show_hidden_word(secret_word, old_letters_guessed))
            else:
                print(":(")
                num_of_tries += 1
                print_hangman(num_of_tries)
                print(show_hidden_word(secret_word, old_letters_guessed))
        else:
            continue
    if num_of_tries == Max_Tries:
        print("You Lost")
        print("The word was: {word}".format(word=secret_word))
    else:
        print("You Won!")


# --------------------------------------------------------

""" 1) Title function:
       - This function prints the title of the game:"""


def print_title():
    print("""  
        _    _
       | |  | |
       | |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __
       |  __  |/ _' | '_ \ / _' | '_ ' _ \ / _' | '_ \\
       | |  | | (_| | | | | (_| | | | | | | (_| | | | |
       |_|  |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                            __/ |
                           |___/""")
    print("Number of false tries: 6")


# --------------------------------------------------------

""" 2) User Input function (file path, keyword-index):
       - This function receives a file path and index from the user and prints the secret word:"""


def user_input():
    file_path = input("Please enter the text file-path: ")
    index = int(input("Please enter index: "))
    return choose_word(file_path, index)


# Helper------------------------------------
def choose_word(file_path, index):
    input_file = open(file_path.strip(' " '), "r")
    data = input_file.read()
    words = data.split(" ")
    words_len = len(words)
    key_word = words[(index - 1) % words_len]
    return key_word.lower()


# --------------------------------------------------------

"""3) Hangman pictures function:
      - This function returns the current picture status of the game:"""


def print_hangman(num_of_tries):
    HANGMAN_PHOTOS = {'1': 'x-------x', '2': """
        x-------x
        |
        |
        |
        |
        |""", '3': '''
        x-------x
        |       |
        |       0
        |
        |
        |''', '4': '''
        x-------x
        |       |
        |       0
        |       |
        |
        |''', '5': '''
        x-------x
        |       |
        |       0
        |      /|\\
        |
        |''', '6': '''
        x-------x
        |       |
        |       0
        |      /|\\
        |      /
        |
    ''', '7': '''
        x-------x
        |       |
        |       0
        |      /|\\
        |      / \\
        |'''}

    print("   " + HANGMAN_PHOTOS[str(num_of_tries)])
    print()


# --------------------------------------------------------

"""4) Updating the guessed letter list:
      - This function checks if the letter is valid and updates the list of letters guessed:"""


def try_update_letter_guessed(letter_guessed, old_letters_guessed):
    if check_valid_input(letter_guessed, old_letters_guessed):
        old_letters_guessed.append(letter_guessed.lower())
        return True
    else:
        sort_list_ans = sorted(old_letters_guessed)
        list_ans = " -> ".join(sort_list_ans)
        print("X")
        print(list_ans)
        return False


# Helper------------------------------------
# - This boolean function checks if guessed letter is valid:
def check_valid_input(letter_guessed, old_letters_guessed):
    letter = letter_guessed.lower()
    if len(letter) == 1 and letter.isalpha() and letter not in old_letters_guessed:
        return True
    return False


# --------------------------------------------------------

"""5) Show Hidden Words function:
      - This function shows the user which letters were guessed correctly and there placement in the secret word.
      - The Indexes of the secret word which were not guessed, will be shown as lines:"""


def show_hidden_word(secret_word, old_letters_guessed):
    for i in range(len(secret_word)):
        if secret_word[i] not in old_letters_guessed:
            secret_word = secret_word.replace(secret_word[i], "_")
    return " ".join(secret_word)


# --------------------------------------------------------

""" 6) Check if user won function:
       - This function checks if the user guessed all the letters of the secret word.
"""


def check_win(secret_word, old_letters_guessed):
    for i in range(len(secret_word)):
        if secret_word[i] not in old_letters_guessed:
            return False
    return True

"""Main function"""


def main():
    Hangman()


if __name__ == "__main__":
    main()