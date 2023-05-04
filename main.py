import sys
import random
from termcolor import colored

def guess_wordle(attempts):
    print("\n")
    print("Enter your guess (", attempts, "remaining ): ")
    guess = input()
    length = len(guess)
    while length != 5:
        print("Please enter a valid guess: ")
        guess = input() 
        length = len(guess)
    guess = guess.upper()
    return guess

def evaluate_attempt(guess, word):
    result = [" "] * 5
    # * < letter is correctly placed
    # + < letter is in word, but incorrectly placed
    # - < letter is not in word

    word_a = list(word)
    guess_a = list(guess)

    for position, letter in enumerate(guess):
        if letter == word[position]:
            if letter in word:
                result[position] = "*"
                guess_a[position] = "0"
                word_a.remove(letter)
    for position, letter in enumerate(guess_a):
        if letter != "0":
            if letter in word_a:
                result[position] = "+"
                guess_a[position] = "0"
                word_a.remove(letter)
            else:
                result[position] = "-"
    
    for position, letter in enumerate(guess):
        if result[position] == "-":
            print(letter, end="")
        elif result[position] == "+":
            print(colored(letter, "yellow"), end="")
        else:
            print(colored(letter, 'green'), end="")

def game_loop(wordlist):
    print("\n")
    print("Selecting a random 5-letter word...")

    word = random.choice(wordlist).upper()

    attempts = 6
    while attempts != 0:
        guess = guess_wordle(attempts)
            
        evaluate_attempt(guess, word)
        attempts -= 1
        if guess == word:
            attempts = 0
            print("\n")
            print("You guessed correctly!")
        elif attempts == 0:
            print("\n")
            print("Out of guesses, game over!")
            print("The word was", word)
    print("Play again? Y/N")
    replay = input().upper()
    while (replay != "Y" and replay != "N"):
        print("Please enter a valid option - Y or N")
        replay = input().upper()
    if replay == "N":
        return False

print("Welcome to Dossy's Wordle!")
print("You have 6 attempts to guess the 5-letter word")
print("If a letter in your guess appears green, then it appears in the word and is in the correct position")
print("If a letter in your guess appears yellow, then it appears in the word but is in the wrong position")

wordlist = open("wordlist.txt", "r").read().split('\n')

while(1):
    play = game_loop(wordlist)
    if play == False:
        break





