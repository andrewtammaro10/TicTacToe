#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 31 20:48:40 2021

@author: drewtammaro
"""

# win check condition      
def wincheck(board):
    # top row
    if board[0][0] == 'X' and board[0][1] == 'X' and board[0][2] == 'X':
        return True
    elif board[0][0] == 'O' and board[0][1] ==  'O' and board[0][2] == 'O':
        return True
    # middle row
    elif board[1][0] == 'X' and board[1][1] == 'X' and board[1][2] == 'X':
        return True
    elif board[1][0] == 'O' and board[1][1] ==  'O' and board[1][2] == 'O':
        return True
    # bottom row
    elif board[2][0] == 'X' and board[2][1] == 'X' and board[2][2] == 'X':
        return True
    elif board[2][0] == 'O' and board[2][1] ==  'O' and board[2][2] == 'O':
        return True
    # left column
    elif board[0][0] == 'X' and board[1][0] == 'X' and board[2][0] == 'X':
        return True
    elif board[0][0] == 'O' and board[1][0] ==  'O' and board[2][0] == 'O':
        return True
    # middle column
    elif board[0][1] == 'X' and board[1][1] == 'X' and board[2][1] == 'X':
        return True
    elif board[0][1] == 'O' and board[1][1] ==  'O' and board[2][1] == 'O':
        return True
    # right column
    elif board[0][2] == 'X' and board[1][2] == 'X' and board[2][2] == 'X':
        return True
    elif board[0][2] == 'O' and board[1][2] ==  'O' and board[2][2] == 'O':
        return True
    # diagonal
    elif board[0][0] == 'X' and board[1][1] == 'X' and board[2][2] == 'X':
        return True
    elif board[0][0] == 'O' and board[1][1] ==  'O' and board[2][2] == 'O':
        return True
    # anti diagonal
    elif board[0][2] == 'X' and board[1][1] == 'X' and board[2][0] == 'X':
        return True
    elif board[0][2] == 'O' and board[1][1] ==  'O' and board[2][0] == 'O':
        return True
    else:
        return False
    
# tic tac toe game
def ttt():
    
    # create empty board
    board = [ ['-','-','-'], ['-','-','-'], ['-','-','-']]
    count = 0
    while count <= 9:
        
        # Check for tie
        if board[0][0] != '-' and board[0][1] != '-' and board[0][2] != '-' and board[1][0] != '-' and board[1][1] != '-' and board[1][2] != '-' and board[2][0] != '-' and board[2][1] != '-' and board[2][2] != '-':
            print('The game is a tie. How fun!')
            break
        
        # If not tied...
        else:
            # X or O goes
            if (count % 2 == 0):
                turn = 'X'
            else:
                turn = 'O'
            
            # Print the board
            for i in range(0,3): print(board[i])
            #print(count)
            
            # Choose a spot
            position = input( "Choose a position: " )
            
            # If it's filled, go again; if it's empty, place the marker
            if position == 'A1':
                if board[0][0] == '-':
                    board[0][0] = turn
                    count += 1
                else:
                    print("Position taken")
                    count = count
                    continue
            elif position == 'B1':
                if board[0][1] == '-':
                    board[0][1] = turn
                    count += 1
                else:
                    print("Position taken")
                    count = count
                    continue
            elif position == 'C1':
                if board[0][2] == '-':
                    board[0][2] = turn
                    count += 1
                else:
                    print("Position taken")
                    count = count
                    continue
            elif position == 'A2':
                if board[1][0] == '-':
                    board[1][0] = turn
                    count += 1
                else:
                    print("Position taken")
                    count = count
                    continue
            elif position == 'B2':
                if board[1][1] == '-':
                    board[1][1] = turn
                    count += 1
                else:
                    print("Position taken")
                    count = count
                    continue
            elif position == 'C2':
                if board[1][2] == '-':
                    board[1][2] = turn
                    count += 1
                else:
                    print("Position taken")
                    count = count
                    continue
            elif position == 'A3':
                if board[2][0] == '-':
                    board[2][0] = turn
                    count += 1
                else:
                    print("Position taken")
                    count = count
                    continue
            elif position == 'B3':
                if board[2][1] == '-':
                    board[2][1] = turn
                    count += 1
                else:
                    print("Position taken")
                    count = count
                    continue
            elif position == 'C3':
                if board[2][2] == '-':
                    board[2][2] = turn
                    count += 1
                else:
                    print("Position taken")
                    count = count
                    continue
            # Any other board spot is invalid
            else:
                print("Invalid board position")
                continue
            
            # If someone has won, print the board and declare a winner
            if wincheck(board):
                for i in range(0,3): print(board[i])
                print("Winner!")
                break
            
            # If no one has one, keep playing
            else:
                continue
            
# Launch the game upon running the program
def main():
    ttt()

####################################################################
if __name__ == "__main__":
    main()


