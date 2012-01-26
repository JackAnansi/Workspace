# Tic Tac Toe multiplayer game


# Print welcome screen
print ( "Welcome to Tic-Tac-Toe!" )


# spaces list holds positions
spaces = [[' ', ' ', ' '],[' ', ' ', ' '],[' ', ' ', ' ']]
taken = set([])     # keeps track of which spaces are taken
gameOver = False # game ending loop variable
playerTurn = 1 # Player 1's turn; negative for Player 2


# drawBoard function draws the complete board
def drawBoard():
    '''The drawBoard function draws the tic-tac-toe board

    A simple set of print statements which draw the board
    and also print the values for spaces[] in each position

    '''
    print( spaces[0][0] + '|' + spaces[0][1] + '|' + spaces[0][2] )
    print( "-----" )
    print( spaces[1][0] + '|' + spaces[1][1] + '|' + spaces[1][2] )
    print( '-----' )
    print( spaces[2][0] + '|' + spaces[2][1] + '|' + spaces[2][2] )



# takeTurn function fills in an X or O
def takeTurn(player, position):
    '''Replaces the value of spaces[][] with an X or O

    Input is the position the character should
    be placed in. This is a string, which is converted
    to an integer

    '''
    letter = 'O'
    if player == 1: letter = 'X'

    if position == 1:
            spaces[0][0] = letter
    elif position == 2:
            spaces[0][1] = letter
    elif position == 3:
            spaces[0][2] = letter
    elif position == 4:
            spaces[1][0] = letter
    elif position == 5:
            spaces[1][1] = letter
    elif position == 6:
            spaces[1][2] = letter
    elif position == 7:
            spaces[2][0] = letter
    elif position == 8:
            spaces[2][1] = letter
    elif position == 9:
            spaces[2][2] = letter
    else: raise NameError ('Strange input')




def checkWin(): 
    '''The checkWin function tests the board for win conditions
    '''
	
    winner = 0		# positive for X, negative for O, or 0 for draw
	
    # horizontal win check
    for i in range(3):
        if spaces[i] == ['X', 'X', 'X']: 
            print ( "'X' wins (horizontal)." )
            return True
        elif spaces[i] == ['O', 'O', 'O']:
            print ( "'O' wins (horizontal)." )
            return True
	
    # vertical win check
    for i in range(3):
        check = ""
        for j in range(3):
            check += spaces[j][i]
			
        if check == "XXX":
            print ( "'X' wins (vertical)." )
            return True
        elif check == "OOO":
            print ( "'O' wins (vertical)." )
            return True
			
    # diagonal win check
    if spaces [0][0] == spaces [1][1] == spaces [2][2] == 'X':
        print ( "'X' wins (diagonal)." )
        return True
    elif spaces [0][0] == spaces [1][1] == spaces [2][2] == 'O':
        print ( "'O' wins (diagonal)." )
        return True
    elif spaces [0][2] == spaces [1][1] == spaces [2][0] == 'X':
        print ( "'X' wins (diagonal)." )
        return True
    elif spaces [0][2] == spaces [1][1] == spaces [2][0] == 'O':
        print ( "'O' wins (diagonal)." )
        return True

    # lost game check
    if taken == {1,2,3,4,5,6,7,8,9}:
        print ( "The game ends in a draw!" )
        return True

    return False            # if no win conditions, continue the game


#main game loop
while gameOver == False:

    drawBoard()                 # draws the game board with x's and o's

    validInput = 0              # loop variable
    while validInput == 0:      # while loop to check for valid input

        # Prints which player's turn it is
        if playerTurn > 0: print( "Player 1")
        else: print( "Player 2")
        
        place = input( "Pick a square (1-9):" ) # player picks square

        # ensures input is an int between 1 and 9
        try:
            place = int(place)
            if place <= 0 or place > 9: print( "Please choose 1-9." )
            elif place in taken: print( "That is already taken." )
            else: validInput = 1
        except:
            print( "Invalid input. Try again." )

        
    takeTurn(playerTurn, place)     # takes turn for player 'playerTurn'
                                    #in position 'place'
                                    
    taken.add(place)                # adds the position to the list of
                                    #used positions

    playerTurn *= -1                # changes turns

    gameOver = checkWin()           # checks for victory conditions
