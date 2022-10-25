# project from https://inventwithpython.com/bigbookpython/project1.html
import random
import sys

def main():
    # Set up the game
    print_game_rules()
    play_bagels()


def play_bagels():
    secret = get_random_digits(3)
    print("I have thought up a number.")
    print(" You have 10 guesses to get it.")

    for i in range(1, 11):
        print("Guess #" + str(i) + ":\n> ", end = "")
        guess = input()
        output = compare_numbers(secret, guess)
        if output == ["You got it!"]:
            print("You got it!")
            print("Do you want to play again? (yes or no)\n> ", end = "")
            again = input()
            if again == "no":
                print("Thanks for playing!")
                return 0
            else:
                play_bagels()
        else:
            for hint in output:
                print(hint, end = " ")
            print("")
    print('''I'm sorry you didn't win.
    The correct number was {}.
    Do you want to play again? (yes or no)\n> '''.format(secret), end = "")
    again = input()
    if again == "no":
        print("Thanks for playing!")
        return 0

# Function to generate a string of random unique digits
def get_random_digits(n):
    digits = list(range(0, 10))
    random_digits = ""
    for i in range(n):
        temp = random.choice(digits)
        random_digits = random_digits + str(temp)
        digits.remove(temp)
    return random_digits


# Set up the game
def print_game_rules():
    print("Bagels, a deductive logic game.")
    print("I am thinking of a 3-digit number. Try to guess what it is.")
    print("Here are some clues:")
    print("When I say:    That means:")
    print("  Pico         One digit is correct but in the wrong position.")
    print("  Fermi        One digit is correct and in the right position.")
    print("  Bagels       No digit is correct.")
    return 0


def compare_numbers(secret, guess):
    result = []
    if secret == guess:
        result.append("You got it!")
        return result
    for i in range(len(guess)):
        if guess[i] in secret:
            if secret.index(guess[i]) == i:
                result.append("Fermi")
            else:
                result.append("Pico")
    if result == []:
        result.append("Bagels")
    # put result in random order
    random.shuffle(result)
    return result


if __name__ == "__main__":
    main()
