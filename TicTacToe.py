import sys
import random

GAMEBOARD_SIZE= 3

class GameBoard:
    board =[]
    #generates empty board
    def __init__(self):
        self.board = [['_','_','_'],['_','_','_'],['_','_','_']]

    #the space on the game board corresponding to the row and col changes to the player character
    def take_turn(self, row, col, player):
        if(self.board[row][col]=='_'):
            self.board[row][col]= player
            return True
        else: 
            return False

    #prints the board
    def display_board(self):
        print("Here is the game state:")
        for x in self.board:
            print(*x, sep='|')
        print()

    #returns true if a win from the inputted player is detected returns false if they haven't won yet, saves on a win
    def detect_win(self,player)->bool:
        #check horizontal
        for i in range(len(self.board)):
            win = True
            for j in range(len(self.board[i])):
                if not(player==self.board[i][j]):
                    win = False
                    break
            if win:
                return win
        #check vertical
        for i in range(len(self.board[0])):
            win = True
            for j in range(len(self.board)):
                if not(player==self.board[j][i]):
                    win = False
                    break
            if win:
                self.save_on_win(player)
                return win
        #check diagonal
        win = True
        for i in range(len(self.board)):
            if not(player==self.board[i][i]):
                win= False
                break
        if win:
            self.save_on_win(player)
            return win
        
        win = True
        for i in range(len(self.board)):
            if not(player==self.board[i][len(self.board)-i-1]):
                win= False
                break
        if win:
            self.save_on_win(player)
            return win 
        #returns a loss
        return win

    #prints the winning game state to a file
    def save_on_win(self,player):
        original_stdout = sys.stdout
        with open('TicTacToeData.txt', 'a') as f:
            sys.stdout = f # Change the standard output to the file created.
            print(f'Player {player} has WON!!')
            self.display_board()
            sys.stdout = original_stdout

    def save_on_draw(self):
        original_stdout = sys.stdout
        with open('TicTacToeData.txt', 'a') as f:
            sys.stdout = f # Change the standard output to the file created.
            print('The game ended in a draw!!')
            self.display_board()
            sys.stdout = original_stdout


class TicTacToe:
    play_again=True
    while play_again:
        
        #checks to see if the input is valid
        while True:
            gamemode=input("Welcome To TicTacToe, do you wish to play with 2 players or against the computer? (enter 'P' for 2 player, enter 'C' for computer) ").upper()
            if gamemode == 'C' or gamemode == 'P':
                break
            else:
                print("Invalid input please try again")
        
        if (gamemode=='P'):
            turn = 0
            board=GameBoard()
            while turn < 9:
                print("Player X take your turn:")
                while True:
                    try:
                        row, col = list(map(int, input("Enter row and column numbers 0-2 (example: ""0 0""): ").split()))
                        if not(board.take_turn(row, col, "X")):
                            raise Exception
                    except:
                        print("Invalid input, try again:  ")
                    else:
                        board.display_board()
                        turn+=1 
                        break

                if(board.detect_win("X")):
                    print("PLAYER X WINS!!!!")
                    break
                if turn == 9:
                    print("THE GAME ENDS IN A DRAW")
                    board.save_on_draw()
                    break

                print("Player O take your turn:")
                while True:
                    try:
                        row, col = list(map(int, input("Enter row and column numbers 0-2 (example: ""0 0""): ").split()))
                        if not(board.take_turn(row, col, "O")):
                            raise Exception
                    except:
                        print("Invalid input, try again:  ")
                    else:
                        board.display_board()
                        turn+=1 
                        break
                if(board.detect_win("O")):
                    print("PLAYER O WINS!!!!")
                    break

            
        if gamemode=="C":
            turn = 0
            board=GameBoard()
            while turn < 9:
                print("Take your turn (You are player X):")
                while True:
                    try:
                        row, col = list(map(int, input("Enter row and column numbers 0-2 (example: ""0 0""): ").split()))
                        if not(board.take_turn(row, col, "X")):
                            raise Exception
                    except:
                        print("Invalid input, try again:  ")
                    else:
                        board.display_board()
                        turn+=1 
                        break
                    
                if(board.detect_win("X")):
                    print("PLAYER X WINS!!!!")
                    break
                if turn == 9:
                    print("THE GAME ENDS IN A DRAW")
                    board.save_on_draw()
                    break

                #computer turn
                print("The computer(O) will now take their turn")
                while True:
                    row = random.randint(0,2)
                    col = random.randint(0,2)
                    if board.take_turn(row, col, "O"):
                        break
                turn += 1
                
                #Computer player win check
                if(board.detect_win("O")):
                    print("THE COMPUTER WINS!!!!")
                    break
                board.display_board()

        while True:
            again=input("do you want to play again? (y or n)").upper()
            if again=="N":
                play_again=False
                break
            elif again=="Y":
                break
            else:
                print("invalid input, please try again")
                    
"""
bord = GameBoard()

bord.display_board()

bord.take_turn(0, 0,'O')
bord.take_turn(0, 0,'O')
bord.take_turn(2, 2,'O')
bord.display_board()
print(bord.detect_win('O'))
"""