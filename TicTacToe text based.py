"""
Project - TicTacToe Assignment 1
Description - This is a game called TicTacToe, which is like connect the dots but with only 3 dots :). This game is a two player game and user can play as many time as they prefer.
"""
# Intial board with '-' for user to fill in.
board =["-"]*10
# Board with position for user to use as refernce board.
position = [None] + list(range(1,10))
# Draws boards for the game. 
def drawBoard(board):
    print(board[1], board[2], board[3])
    print(board[4], board[5], board[6])
    print(board[7], board[8], board[9])
    print()
#Checks user input and is it valid or not.
def getMove(board,name):
    while True:
        try:
            user_input = int(input(name + " it's your turn. Enter a move (1 - 9) "))
            if user_input < 1 or user_input > 9 or board[user_input] != '-':
                print(" Invalid move. Please try again using the position chart below! ")
                drawBoard(position)
            else:
                return user_input
        except ValueError:
            print("\nThat is not a number. Try again!")
#Checks if user won 
def win(board,symbol):
    # The winning combinations in all directions.
             return ((board[7] == symbol and board[8] == symbol and board[9] == symbol) or # across the bottom
                     (board[4] == symbol and board[5] == symbol and board[6] == symbol) or # across the middle
                     (board[1] == symbol and board[2] == symbol and board[3] == symbol) or # across the top
                     (board[7] == symbol and board[4] == symbol and board[1] == symbol) or # down the left side
                     (board[8] == symbol and board[5] == symbol and board[2] == symbol) or # down the middle
                     (board[9] == symbol and board[6] == symbol and board[3] == symbol) or # down the right side
                     (board[7] == symbol and board[5] == symbol and board[3] == symbol) or # diagonal
                     (board[9] == symbol and board[5] == symbol and board[1] == symbol)) # diagonal
#Checks if the game ends in a tie.
def tie(board):
    for i in board:
        if i == '-':
            return False
    return True
#Calculation function for the game.
def main():
    print("Let's play TicTacToe. \n")
    #User inputs
    player1 = input("Enter the name of player 1: \n")
    player2 = input("Enter the name of player 2: \n")
    #Lets the user pick their own symbols 
    symbol=''
    while not (symbol == 'X' or symbol == 'O'):
        try:
            player1_symbol = input("Player 1 please enter X or O to be used as your symbols for the game! \n").upper()
            player2_symbol = input("Player 2 please enter X or O to be used as your symbols for the game! \n").upper()
        except ValueError:
            print("\n Please enter X or O! ")
        break
    #Shows position board and the game board
    print("Enter your marks using the board positions shown below:")
    drawBoard(position)
    print("\nGame board")
    drawBoard(board)
    #Checks both of the user inputs 
    while True:
    #Player 1 input.
            user_input = getMove(board,player1)
            board[user_input]=player1_symbol
            drawBoard(board)
    #Checks if the player1 won.
            if win(board,player1_symbol):
                print(player1 + " wins!")
                break
    #Checks if the game is tied.
            if tie(board):
                print("Tie game!")
                break
    #Player 2 input.
            user_input = getMove(board, player2)
            board[user_input] = player2_symbol
            drawBoard(board)
     #Checks if the player2 won.
            if win(board, player2_symbol):
                print(player2 + " wins!")
                break
    #Checks if the game is tied.
            if tie(board):
                print("Tie game!")
                break
#Checks if everthing works and then it runs.
while True:
    #Calls the main funcion after checking everything is true
    main()
    #Restart the game!
    if input("Do you want to play again (y or n)?") != 'y':
        break
    #Resets the game if user presses y!
    board =["-"]*10
    drawBoard(board)
