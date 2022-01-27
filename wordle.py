import os
import random
from termcolor import colored, COLORS

DICTIONARY_FILE = r"all_dictionary_words.txt"
MENU_STR = "Welcome to WORDLE!\n" \
           "Choose your next action from the menu:\n" \
           "'p' - play\n" \
           "'e' - exit\n" \
           "Submit your choice: "
EXIT = 'e'
PLAY = 'p'
KNOWN_COMMANDS = [PLAY, EXIT]
REVEAL_ANSWER_CODE = '!@#!@#'


def get_dictionary(text_file):
    with open(text_file, "r") as f:
        words = f.read().splitlines()
    return words


def check_for_reveal_code(guess, answer):
    if guess == REVEAL_ANSWER_CODE:
        print(colored(answer, "red"))
        return True
    return False
    

def play_round(answer, dictionary, strikes=6):
    for strike in range(1, strikes+1):
        guess = input("TYPE YOUR GUESS: ").strip().upper()
        if check_for_reveal_code(guess, answer):
            return None
        while guess not in dictionary:
            print(f"WORD NOT RECOGNIZED!\n")
            guess = input("TYPE YOUR GUESS: ").strip().upper()
            if check_for_reveal_code(guess, answer):
                return None
        guess_colored = []
        correct = 0
        for index, letter in enumerate(guess):
            letter_color = "white"
            if answer[index] == letter:
                letter_color = "green"
                correct += 1
            elif letter in answer:
                letter_color = "yellow"
            guess_colored.append(colored(letter.upper(), letter_color))
        print(f"{strike}/{strikes} - {' '.join(guess_colored)}")
        if correct == len(answer):
            return True
    return False

    
def main():
    os.system("cls")
    dictionary = get_dictionary(DICTIONARY_FILE)
    word_bank = dictionary.copy()
    action = None
    while not action == EXIT:
        action = input(MENU_STR)
        if action == PLAY:
            answer = random.choice(word_bank)
            word_bank.remove(answer)
            result = play_round(answer=answer, dictionary=dictionary)
            if result is True:
                print(colored("YAYYYY!!\n", "cyan"))
            elif result is False:
                print(colored("GAME OVER :(\n"
                              f"The answer was: {answer}", "red"))
        elif action not in KNOWN_COMMANDS:
            print("MUST SUBMIT A VALID OPTION!\n")


if __name__ == '__main__':
    os.system("color")
    main()