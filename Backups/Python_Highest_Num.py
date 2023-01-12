# The Highest Number Game  -  Dylan Gartin 

import random # The random function which is needed to select from the lower_Bound_Bound_Bound and upper_bound bounds
import math # Math makes it where i can use the log function in my game so i can use it to choose a fair ammount of attempts

#WORK NEEDED - Must make it a Class

print("Hey Kiddo Welcome To Is-it-int, Number Gameo! Pick some Interger Numbers to establish the range your playing under!\n") # Flavor Text Print Statement giving game instructions 

# WORK NEEDED - a try and Catch for a value Error
lower_bound = int(input("Give me your lowest possible Number: "))  # Choose a Number to be the lower_Bound bounding Box of the game.

# WORK NEEDED - a try and Catch for a Value Error May need another if is to small
upper_bound = int(input("Give me your Highest possible Number:  ")) # Choose a number to be the highest boundry block

# Game Setup Variables 
TheChoosen = random.randint(lower_bound, upper_bound) # Selects a random int in the range 
attempts = round(math.log(upper_bound - lower_bound + 1,2)) # this makes the numbers of attempts a nice fair value
count = 0 # starts the number of guesses at 0 and this will increment each guess

print("\nYou've only ", attempts, " chances to guess that bad int, good luck!\n") # does the log of upper_bound - lower_Bound + 1 , e = 2.7 ish, could make it harder by allowing a challenege rating here
print("-" * 100) # formatting output

# Number of Guesses allowed by the system is less then the number of counts
while count < attempts :
    count += 1 # add one to the count as to 

	# taking guessing number as input - this will need a try catch for value error
    guess = int(input("Guess that number or make a blunder!: "))

	# The following if statemnet below will output the feedback needed for the numbers

    if TheChoosen  == guess: # If the numbers 
        print("-" * 100) # formatting output
        print("Darn it you got it, and in only", count, " try or tries, Congrats, I guess.") # print your victory statement 
        # WORK NEEDED - Make where it send these results
        break # Once correct break the loop
    elif TheChoosen  > guess: #  if the choosen number is Higher then your guess
        print("Nope your going for the floor kid, go a little lower!") # Should Guess higher! this guy is a liar and try to throw you off the number by saying advice that makes you think the other way
    elif TheChoosen  < guess: #  if the choosen number is lower_Bound then your guess
        print("Nope your going for the clouds kid, go a little higher!") # Should guess lower_Bound! HE A CON MAN A CONNNN

#  Once your over the max number of tries
if count >= attempts:
    print("-" * 100) # formatting output
    print("\nThe number is,", TheChoosen , "Ooo, sorry, Better Luck Next time Kid!") # output the failure text 
    # WORK NEEDED - Make where it send these results 

