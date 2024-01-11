from art import logo
from random import randint

EASY_LEVEL_TRIES = 10
HARD_LEVEL_TRIES = 5


def check_answer(guess, ans, tries):
    """
    Checks answer against guess and returns the number of tries remaining
    :param guess: guess
    :param ans: answer
    :param tries: number of tries before checking
    :return: number of tries after checking guess against answer.
    """
    if guess > ans:
        print("Too high.")
        return tries - 1
    elif guess < ans:
        print("Too low.")
        return tries - 1
    else:
        print(f"You got it! The answer was {ans}.")
        return tries


def start_game(tries, ans):
    guess = 0
    while guess != ans:
        print(f"You have {tries} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))
        tries = check_answer(guess, ans, tries)

        if tries == 0:
            print("You've run out of guesses, you lose.")
            return
        elif guess != ans:
            print("Guess again.")


def get_number_attempts():
    """
    Returns the number of tries the user has if the level is easy or hard
    :return: the number of tries the user can guess
    """
    level = input('Choose a difficulty. Type "easy" or "hard": ')
    if level == "easy":
        return EASY_LEVEL_TRIES
    else:
        return HARD_LEVEL_TRIES


if __name__ == '__main__':
    print(logo)
    answer = randint(1, 100)
    print("Welcome to the Number Guessing Game! I am thinking of a number between 1 - 100.")
    print(f"Pssst, the correct answer is {answer}")
    attempts = get_number_attempts()
    start_game(attempts, answer)
