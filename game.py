import random

HANGMAN = [
    '''
    +---+
        |
        |
        |
       ===
    ''',
    '''
    +---+
    o   |
        |
        |
       ===
    ''',
    '''
    +---+
    o   |
    |   |
        |
       ===
    ''',
    '''
    +---+
    o   |
   /|   |
        |
       ===
    ''',
    '''
    +---+
    o   |
   /|\  |
        |
       ===
    ''',
    '''
    +---+
    o   |
   /|\  |
   /    |
       ===
    ''',
    '''
    +---+
    o   |
   /|\  |
   / \  |
       ===
    '''
]

#List of car brand names
cars = 'lamborghini ferrari porsche mclaren bugatti maserati lotus astonmartin hennessey koenigsegg ford chevrolet jeep subaru dodge toyota volkswagen honda kia nissan landrover rollsroyce mercedesbenz audi acura jaguar cadillac bmw'.split()

# Returns a car string from a Dictionary passed in key
def getRandomCar(carList):
    selectCar = random.randint(0, len(carList) - 1)
    return carList[selectCar]

# Prints the hangman game
def showHangman(wrongLetters, correctLetters, secretWord):
    print(HANGMAN[len(wrongLetters)])
    print("Guess the car brand\n")

    print('Wrong letters you have already entered:', end=' ')

    for letter in wrongLetters:
        print(letter, end=' ')
    print()

    spaces = '_' * len(secretWord)

    # Fills in the blank spaces with the correct letter guess
    for guess in range(len(secretWord)):
        if secretWord[guess] in correctLetters:
            spaces = spaces[:guess] + secretWord[guess] + spaces[guess + 1:]

    # Shows each letter in the secret word
    for letter in spaces:
        print(letter, end=' ')
    print()

# Returns the letter the player has entered
def getGuess(playerGuess):
    while True:
        guess = input("\nPlease enter a letter. ")
        guess = guess.lower()

        # A check to make sure that the player has only entered a single charater and not anything else like a number.
        if len(guess) != 1:
            print("Please only enter a single letter.")

        elif guess in playerGuess:
            print(f"You have already guessed {guess}. Please choose another letter.")

        elif guess not in 'abcdefghijklmnopqrstuvwxyz':
            print("Sorry you can only enter a letter from the alphabet.")

        else: return guess

# If you want to play again
def playAgain():
    play = input("Do you want to play again (yes or no)? ")

    if play == "yes" or play == 'y':
        return True

    elif play == "no" or play == 'n':
        return False

wrongLetters = ''
correctLetters = ''
secretWord = getRandomCar(cars)
endOfGame = False

while True:
    showHangman(wrongLetters, correctLetters, secretWord)

    guess = getGuess(wrongLetters + correctLetters)

    if guess in secretWord:
        correctLetters = correctLetters + guess

        #A check to see if the player has won
        foundWord = True
        for letter in range(len(secretWord)):
            if secretWord[letter] not in correctLetters:
                foundWord = False
                break

        if foundWord:
            print(f"\nCorrect!!! The secret word is {secretWord}. Congratulations you have won!\nYou only got " + str(len(wrongLetters)) + " letters wrong.\n")
            endOfGame = True

    else:
        wrongLetters = wrongLetters + guess

        # A check to stop asking the player when they have run out of guesses and lost the game.
        if len(wrongLetters) == len(HANGMAN) - 1:
            showHangman(wrongLetters, correctLetters, secretWord)
            print("Sorry you have ran out of guesses,\nYou got " + str(len(wrongLetters)) + " wrong guesses and " + str(len(correctLetters)) + ' correct guesses,\nThe car brand was "' + secretWord + '"\n')
            endOfGame = True

    # After the game is over the player is asked if they want to play again
    if endOfGame:
        if playAgain():
            wrongLetters = ''
            correctLetters = ''
            endOfGame = False
            secretWord = getRandomCar(cars)
        else:
            break

file = open("hangman.txt", "wt")
file.write("You got " + str(len(wrongLetters)) + " letters wrong and those letters were " + wrongLetters + " and you got " + str(len(correctLetters)) + " letters correct and those letters were " + correctLetters + ". The car brand was " + secretWord)
file.close

