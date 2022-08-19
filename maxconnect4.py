#!/usr/bin/env python

# Written by Chris Conly based on C++
# code provided by Dr. Vassilis Athitsos
# Written to be Python 2.4 compatible for omega

import sys
from MaxConnect4Game import *

def oneMoveGame(currentGame):
    if currentGame.pieceCount == 42:    # Is the board full already?
        print('BOARD FULL\n\nGame Over!\n')
        sys.exit(0)

    currentGame.aiPlay() 

    print('Game state after move:')
    currentGame.printGameBoard()

    currentGame.countScore()
    print('Score: Player 1 = %d, Player 2 = %d\n' % (currentGame.player1Score, currentGame.player2Score))

    currentGame.printGameBoardToFile()
    currentGame.gameFile.close()


def interactiveGame(currentGame, firstPlayer):
    column = 0

    firstCheck = True
    while True:
        humanFile = open("human.txt", "w")
        computerFile = open("computer.txt", "w")
        # if Ai is first player than play Ai first
        if firstPlayer == 'computer-next' and firstCheck == True:
            currentGame.printGameBoard()
            print('Score: Player 1 = %d, Player 2 = %d\n' % (currentGame.player1Score, currentGame.player2Score))
            if currentGame.pieceCount == 42:
                break
            currentGame.aiPlay()
            currentGame.printGameBoardToFilePlayer(computerFile)
            firstCheck = False


        currentGame.printGameBoard()
        currentGame.countScore()
        print('Score: Player 1 = %d, Player 2 = %d\n' % (currentGame.player1Score, currentGame.player2Score))
        if currentGame.pieceCount == 42:
            break

        # error handing in case input was not a legal number or column is full
        column = input("Enter the column you wish to add a piece too. (1-7): ")
        while column.isnumeric() == False or (int(column) > 7 or int(column) < 1):
            column = input("input was not a number in the range of (1-7). Please try again: ")
        result = currentGame.playPiece(int(column) - 1)
        while (result == None):
            column = input("Please try again: ")
            try:
                int(column)
            except:
                print("input was not a number in the range of (1-7).")
            else:
                if int(column) >= 1 and int(column) <= 7:
                    result = currentGame.playPiece(int(column) - 1)
                else: 
                    print("input was not in the range of (1-7).")
        
        # after human makes his choice, switch turns
        if currentGame.currentTurn == 1:
            currentGame.currentTurn = 2
        else:
            currentGame.currentTurn = 1
        # erase file contents and add new game board 
        humanFile.truncate(0)
        humanFile.seek(0)
        currentGame.printGameBoardToFilePlayer(humanFile)

        currentGame.printGameBoard()
        currentGame.countScore()
        print('Score: Player 1 = %d, Player 2 = %d\n' % (currentGame.player1Score, currentGame.player2Score))
        if currentGame.pieceCount == 42:
            break
        currentGame.aiPlay()

        # erase file contents and add new game board 
        computerFile.truncate(0)
        computerFile.seek(0)
        currentGame.printGameBoardToFilePlayer(computerFile)




def main(argv):
    # Make sure we have enough command-line arguments
    if len(argv) != 5:
        print('Four command-line arguments are needed:')
        print('Usage: %s interactive [input_file] [computer-next/human-next] [depth]' % argv[0])
        print('or: %s one-move [input_file] [output_file] [depth]' % argv[0])
        sys.exit(2)

    game_mode, inFile = argv[1:3]

    if not game_mode == 'interactive' and not game_mode == 'one-move':
        print('%s is an unrecognized game mode' % game_mode)
        sys.exit(2)
    currentGame = maxConnect4Game(argv[4], argv[3]) # Create a game

    # Try to open the input file
    try:
        currentGame.gameFile = open(inFile, 'r')
    except IOError:
        sys.exit("\nError opening input file.\nCheck file name.\n")

    # Read the initial game state from the file and save in a 2D list
    file_lines = currentGame.gameFile.readlines()
    currentGame.gameBoard = [[int(char) for char in line[0:7]] for line in file_lines[0:-1]]
    currentGame.currentTurn = int(file_lines[-1][0])
    currentGame.gameFile.close()

    print('\nMaxConnect-4 game\n')
    print('Game state before move:')
    currentGame.printGameBoard()

    # Update a few game variables based on initial state and print the score
    currentGame.checkPieceCount()
    currentGame.countScore()
    print('Score: Player 1 = %d, Player 2 = %d\n' % (currentGame.player1Score, currentGame.player2Score))

    if game_mode == 'interactive':
        interactiveGame(currentGame, argv[3]) # Be sure to pass whatever else you need from the command line
    else: # game_mode == 'one-move'
        # Set up the output file
        outFile = argv[3]
        try:
            currentGame.gameFile = open(outFile, 'w')
        except:
            sys.exit('Error opening output file.')
        oneMoveGame(currentGame) # Be sure to pass any other arguments from the command line you might need.


if __name__ == '__main__':
    main(sys.argv)




