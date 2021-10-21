#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 31 20:48:40 2021

@author: drewtammaro
"""

position = input( "Choose a position: " )
print( position )


spaces = ['A1','B1','C1','A2','B2','C2','A3','B3','C3']
#{space: '_' for space in board}
board = dict.fromkeys(spaces)
#board = {boardlist: '_' for boardlist[0:8]}
print(board)

P1 = 'X'
P2 = 'O'


def ttr(board,start):
    if None in board.values():
        position = input( "Choose a position: " )
        print( position )
        if position in  board:
            print('Real spot broseph')
            
        else:
            print('Thats not gonna get it done')
    else:
        print('The game is a tie')
        
        
board = [ ['-','-','-'], ['-','-','-'], ['-','-','-']]
for i in range(0,3): print(board[i])

def ttt():
    board = [ ['-','-','-'], ['-','-','-'], ['-','-','-']]
    count = 0
    for i in range(10):
        if count == 9:
            print("The game is a tie. How fun!")
            break
        else:
            if (count % 2 == 0):
                turn = 'X'
            else:
                turn = 'O'
            for i in range(0,3): print(board[i])
            print(count)
            position = input( "Choose a position: " )
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
            else:
                print("Invalid board position cuh")
                continue
            if wincheck(board):
                for i in range(0,3): print(board[i])
                print("Winner!")
                break
            else:
                continue
    # else:
    #     print("The game is a tie. How fun!")
        
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


