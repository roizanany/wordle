import argparse
from wordle import DICTIONARY_FILE

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("word", help="the word you want to add")
    args = parser.parse_args()
    word = args.word.upper()
    if not len(word) == 5:
        raise ValueError(f"THE WORD '{word}' IS INVALID! MUST BE 5 LETTERS LONG")
    elif not word.isalpha():
        raise ValueError(f"ONLY ENGLISH LETTERS PLEASE!")
    with open(DICTIONARY_FILE, "r") as f:
        words = f.read().splitlines()
    if word not in words:
        words.append(word)
    words.sort()
    new_words_str = "\n".join(words)
    with open(DICTIONARY_FILE, "w") as f:
        f.write(new_words_str)
    print(f"WORD '{word}' ADDED :)")