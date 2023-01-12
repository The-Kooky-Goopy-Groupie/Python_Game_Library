# The Game-A-Tron (Game Module Handler)
import math #honestly is just here to test imports work
import Py_High_Num_Fun  # bring in the game function 

def playgames(WishtoGame):   # Make the style -> lowercase functions 
    while True: # forces you to pass this check to continue
        try: # try the int input
            WishtoGame = str(input("Would you like to play a game? Type in 'y' or 'n' for yes and no:  ")) # Choose a number to be the highest boundry block
            print("Choice: ", WishtoGame)
            if WishtoGame == "y" : # check wish to game is either y or n
                print ("Got it Booting up Game Choice Sequence:")
                break
            elif WishtoGame == "n" :  # if told no
                print ("Understood we are shutting down then!") # display shutdown message
                break
            else:
                raise Exception # if so go to the exception
        except Exception:
            print ("I can only accept either 'y' or 'n'  as responses ")
    return WishtoGame

def selectgames(Int_based_value, Output_Msg): #Works somewhat like the previous one
    while True: # this forces you to pass this check to continue 
        try: # try the int input
            Int_based_value = int(input(Output_Msg))  # Choose a Number to be the lower_Bound bounding Box of the game.
            if Int_based_value == 1 : # make sure is not a bigger then lower bound one
                print("Starting Game 1: ")
                Py_High_Num_Fun.HighestNum().Main_Highest_Num() # YOU NEED TO CALL THE FUNCTION OF IT
                # Py_High_Num_Fun.high_num # call the high num game to the file and play it
                break
            elif Int_based_value == 2 : # make sure is not a bigger then lower bound one
                print("Starting Game 2: ")
                # Game Goes Here
                break
            elif Int_based_value == 3 : # make sure is not a bigger then lower bound one
                print("Starting Game 3: ")
                # Game
                break     
        except Exception as e: # get any value errors 
            print("The game your try to access seems to not exist yet...") # error msg for failure
            print(e)
    return Int_based_value


class GameTron:
    UserChoice = 'x' # sets the users game choice to x by default
    UserChoice = playgames(UserChoice) # choose yes or no for the user choice
    while UserChoice == 'y':  # user choice 
        print("-*"*50) # style
        print("Choose a game to call forth by picking the corsponding list: ")
        print("-*"*50) # style
        Default_Game_Value = 0 # a default value needed for an input so game selected can be changed
        GameSelected = selectgames(Default_Game_Value,"The games you can select from are:\n \t '1' for Highest Number Game \n \t '2' for Hangman\n \t '3' for Tic Tac Toe\n \t Put your input here:  ") # Game output list codes
        print(GameSelected) # test print to make sure the game selected has updated properly 
        UserChoice = 'x' # reset the bool back to default after the game is done
        print(" WAHOO IT's A ME MARIO - you have played a game! Congratulations") # announce that a game is finished
        UserChoice = playgames(UserChoice)  # check to continue the while loop
        # Current issue it will go and play one of the games once but then it won't play it again on the second pass 
UltimateGamer = GameTron  # invoking of the gamer class 