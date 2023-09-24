import random

def choose_word():
    words = ["apple", "banana", "cherry", "date", "elderberry", "fig", "grape", "honeydew", "kiwi", "lemon"]
    return random.choice(words)

def display_word(word, guessed_letters):
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter
        else:
            display += "_"
    return display

def draw_hangman(attempts):
    hangman = [
        "  _____",
        "  |   |",
        "  |",
        "  |",
        "  |",
        "  |",
        "  |",
        "  |",
        "__|__"
    ]
    if attempts < 7:
        hangman[2] = "  |   O"
    if attempts == 2:
        hangman[3] = "  |   |"
    elif attempts == 3:
        hangman[3] = "  |  /|"
    elif attempts >= 4:
        hangman[3] = "  |  /|\\"
    if attempts == 5:
        hangman[4] = "  |  /"
    elif attempts >= 6:
        hangman[4] = "  |  / \\"
    for line in hangman:
        print(line)

def main():
    word = choose_word()
    guessed_letters = []
    attempts = 0
    max_attempts = 6

    print("Welcome to Hangman!")
    
    while True:
        print("\n" + display_word(word, guessed_letters))
        guess = input("Guess a letter: ").lower()
        
        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input. Please enter a single letter.")
            continue
        
        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue
        
        guessed_letters.append(guess)
        
        if guess in word:
            print("Good guess!")
        else:
            print("Wrong guess!")
            attempts += 1
            draw_hangman(attempts)
        
        if "_" not in display_word(word, guessed_letters):
            print("Congratulations! You've guessed the word: " + word)
            break
        
        if attempts == max_attempts:
            print("Sorry, you ran out of attempts. The word was: " + word)
            break

if __name__ == "__main__":
    main()
import random

def choose_word():
    words = ["apple", "banana", "cherry", "date", "elderberry", "fig", "grape", "honeydew", "kiwi", "lemon"]
    return random.choice(words)

def display_word(word, guessed_letters):
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter
        else:
            display += "_"
    return display

def draw_hangman(attempts):
    hangman = [
        "  _____",
        "  |   |",
        "  |",
        "  |",
        "  |",
        "  |",
        "  |",
        "  |",
        "__|__"
    ]
    if attempts < 7:
        hangman[2] = "  |   O"
    if attempts == 2:
        hangman[3] = "  |   |"
    elif attempts == 3:
        hangman[3] = "  |  /|"
    elif attempts >= 4:
        hangman[3] = "  |  /|\\"
    if attempts == 5:
        hangman[4] = "  |  /"
    elif attempts >= 6:
        hangman[4] = "  |  / \\"
    for line in hangman:
        print(line)

def main():
    word = choose_word()
    guessed_letters = []
    attempts = 0
    max_attempts = 6

    print("Welcome to Hangman!")
    
    while True:
        print("\n" + display_word(word, guessed_letters))
        guess = input("Guess a letter: ").lower()
        
        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input. Please enter a single letter.")
            continue
        
        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue
        
        guessed_letters.append(guess)
        
        if guess in word:
            print("Good guess!")
        else:
            print("Wrong guess!")
            attempts += 1
            draw_hangman(attempts)
        
        if "_" not in display_word(word, guessed_letters):
            print("Congratulations! You've guessed the word: " + word)
            break
        
        if attempts == max_attempts:
            print("Sorry, you ran out of attempts. The word was: " + word)
            break

if __name__ == "__main__":
    main()
import random

def choose_word():
    words = ["apple", "banana", "cherry", "date", "elderberry", "fig", "grape", "honeydew", "kiwi", "lemon"]
    return random.choice(words)

def display_word(word, guessed_letters):
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter
        else:
            display += "_"
    return display

def draw_hangman(attempts):
    hangman = [
        "  _____",
        "  |   |",
        "  |",
        "  |",
        "  |",
        "  |",
        "  |",
        "  |",
        "__|__"
    ]
    if attempts < 7:
        hangman[2] = "  |   O"
    if attempts == 2:
        hangman[3] = "  |   |"
    elif attempts == 3:
        hangman[3] = "  |  /|"
    elif attempts >= 4:
        hangman[3] = "  |  /|\\"
    if attempts == 5:
        hangman[4] = "  |  /"
    elif attempts >= 6:
        hangman[4] = "  |  / \\"
    for line in hangman:
        print(line)

def main():
    word = choose_word()
    guessed_letters = []
    attempts = 0
    max_attempts = 6

    print("Welcome to Hangman!")
    
    while True:
        print("\n" + display_word(word, guessed_letters))
        guess = input("Guess a letter: ").lower()
        
        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input. Please enter a single letter.")
            continue
        
        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue
        
        guessed_letters.append(guess)
        
        if guess in word:
            print("Good guess!")
        else:
            print("Wrong guess!")
            attempts += 1
            draw_hangman(attempts)
        
        if "_" not in display_word(word, guessed_letters):
            print("Congratulations! You've guessed the word: " + word)
            break
        
        if attempts == max_attempts:
            print("Sorry, you ran out of attempts. The word was: " + word)
            break

if __name__ == "__main__":
    main()
