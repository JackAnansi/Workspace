# Tic Tac Toe multiplayer game

# spaces array holds positions
spaces = [" "]* 9

gameOver = False # game ending loop variable
playerTurn = 1 # Player 1's turn; negative for Player 2
validInput = 0  #loop var to ensure valid input


# drawBoard function draws the complete board
def drawBoard():
    '''The drawBoard function draws the tic-tac-toe board

    A simple set of print statements which draw the board
    and also print the values for spaces[] in each position

    '''
    print( spaces[0] + '|' + spaces[1] + '|' + spaces[2] )
    print( "-----" )
    print( spaces[3] + '|' + spaces[4] + '|' + spaces[5] )
    print( '-----' )
    print( spaces[6] + '|' + spaces[7] + '|' + spaces[8] )

# takeTurn function fills in an X or O
def takeTurn(player, position):
    '''Replaces the value of spaces[n] with an X or O

    First input is player number, to determine whether
    an X or O should be placed. This is an int.

    Second input is the position the character should
    be placed in. This is a string, which is converted
    to an integer

    '''
    #position = int(position)
    letter = 'O'
    if player == 1: letter = 'X'
    spaces[position-1] = letter

# checkWin function checks for victory
def checkWin():
    '''Checks for victory conditions on the game board.

    There has to be an easier way of doing this...

    '''
    if spaces[0] == spaces[1] == spaces[2] == 'X':
        gameOver = True
        print( "Player 1 Wins!" )


# Start of program; welcome message and draw empty board
print(" Welcome to Tic Tac Toe!\n ")

# Game loop
while gameOver == False:

    drawBoard()         # draws the complete board

    while validInput == 0:      # while loop to check for valid input

        print( "Player " + str(playerTurn) )
        place = input( "Pick a square (1-9):" ) # player picks square

        try:
            place = int(place)
            if place <= 0 or place > 9: print( "Please choose 1-9." )
            else: validInput = 1
        except:
            print( "Invalid input. Try again." )

        

        
    takeTurn(playerTurn, place)     # takes turn for player 'playerTurn'
                                    # in position 'place'
    
    if playerTurn == 1: playerTurn = 2
    elif playerTurn == 2: playerTurn = 1

    validInput = 0
    checkWin()
