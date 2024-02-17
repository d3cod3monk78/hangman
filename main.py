import random
from words import words


def get_valid_word(random_words):
    word = random.choice(random_words)

    while '-' in word or ' ' in word:
        word = random.choice(random_words)

    return word.upper


def hangman():
    pass

