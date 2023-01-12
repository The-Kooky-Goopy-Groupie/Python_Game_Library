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

#Dictionary of cars names
cars = {'Super': 'lamborghini ferrari porsche mclaren bugatti maserati lotus astonmartin hennessey koenigsegg'.split(), 
'Common': 'ford chevrolet jeep subaru dodge toyota volkswagen honda kia nissan'.split(), 
'Luxury': 'landrover rollsroyce mercedesbenz audi acura jaguar cadillac'.split()}

# Returns a car string from a Dictionary passed in key
def getRandomCar(carDict):
    # Selects a random key from the dictionary
    carKey = random.choice(list(carDict.keys()))

    # Selects a random car name from key's in the dictionary
    selectCar = random.randint(0, len(carDict[carKey]) - 1)

    # The function returns a list with two items
    return [carDict[carKey][selectCar], carKey]

# Prints the hangman game
def showHangman(wrongLetters, correctLetters, secretWord):
    print(HANGMAN[len(wrongLetters)])
    print()

    print('Wrong letters you have entered:', end=' ')
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
            print("You have already guessed that letter. Please choose another letter.")

        elif guess not in 'abcdefghijklmnopqrstuvwxyz':
            print("Sorry you can only enter a letter from the alphabet.")

        else: return guess

# If you want to play again
def playAgain():
    play = input("Do you want to play again (yes or no)? ")

    return play.startswith('y')

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
            print(f"Correct!!! The secret word is {secretWord}. Congratulations you have won!")
            endOfGame = True

    else:
        wrongLetters = wrongLetters + guess

        # A check to stop asking the player when they have run out of guesses and lost the game.
        if len(wrongLetters) == len(HANGMAN) - 1:
            showHangman(wrongLetters, correctLetters, secretWord)
            print("Sorry you have ran out of guesses\n" + str(len(wrongLetters)) + "wrong guesses and " + str(len(correctLetters)) + 'correct guesses, the word was "' + secretWord + '"')
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