# Tic Tac Toe multiplayer game

#spaces array holds positions
spaces = [" "]* 9

gameOver = False # game ending loop variable
playerTurn = 1 # Player 1's turn


#drawBoard function draws the complete board
def drawBoard():
    print( spaces[0] + '|' + spaces[1] + '|' + spaces[2] )
    print( "-----" )
    print( spaces[3] + '|' + spaces[4] + '|' + spaces[5] )
    print( '-----' )
    print( spaces[6] + '|' + spaces[7] + '|' + spaces[8] )

#takeTurn function fills in an X or O
def takeTurn(player, position):
    letter = 'O'
    if player == 1: letter = 'X'
    spaces[position-1] = letter

#checkWin function checks for victory
def checkWin():


#Start of program; welcome message and draw empty board
print(" Welcome to Tic Tac Toe!\n ")

#Game loop
while gameOver == False:
    drawBoard()
    place = input( "Player " + str(playerTurn) + ", pick a square (1-9)")
    place = int(place)
    takeTurn(playerTurn, place)
    if playerTurn == 1: playerTurn = 2
    else: playerTurn = 1
    checkWin()
