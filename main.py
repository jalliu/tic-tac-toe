#Tic-Tac-Toe Beginner Project
#8/1/2021, guide for hints: https://www.techwithtim.net/tutorials/python-programming/tic-tac-toe-tutorial/


#create the game board, board[0] will not be used
board = [' ' for space in range(10)]

def main():
    print('Welcome to Tic-Tac-Toe. In this game, two players are  represented by either a \'X\' or \'O\'. \n'
          'Whichever player is the first to place three of their marks in a horizontal, vertical, or diagonal \n'
          'straight line will win.')
    print()
    print('The board is shown below. The positions are numbered 1-9, starting from the top left and continuing down '
          ' each row.')
    print('EX: The bottom left of the board is position 7.')
    print('-----------------------------------------------')
    print_board()

    while not(is_board_filled(board)):
        if not(is_Winner('O')):
            player_move('X')
            print_board()
        else:
            print('Player \'O\' is the winner!')
            break

        if not(is_Winner('X')):
            player_move('O')
            print_board()
        else:
            print('Player \'X\' is the winner!')
            break

    if(is_board_filled(board)):
        print('The game is a tie!')


#------------------------------------------------------
#print the game board
def print_board():
    print('New Round:')
    print('|' + board[1] + '|' + board[2] + '|' + board[3] + '|')
    print('|' + board[4] + '|' + board[5] + '|' + board[6] + '|')
    print('|' + board[7] + '|' + board[8] + '|' + board[9] + '|')

#player moves
def player_move(symbol):
    run = True
    while(run):
        input_position = input('Please input where you would like to place a ' + symbol + ' (1-9) ')
        try:
            input_position = int(input_position)
            if(is_move_valid(symbol, input_position)):
                run = False
                place_move(symbol, input_position)
            else:
                print('That position is either already filled or not in range (1-9). Please make a valid move.')
        except:
            print('Please input a NUMBER from 1-9.')

#place a move
def place_move(symbol, position):
    board[position] = symbol

#tests if move is valid
def is_move_valid(symbol, position):
    if 1 <= position <= 9 and board[position] == ' ':
            return True
    else:
        return False

#test if board is filled:
def is_board_filled(board):
    if board.count(' ') > 1:
        return False
    else:
        return True


#checks to see who won
def is_Winner(symbol):
    return ((board[1] == symbol and board[2] == symbol and board[3] == symbol) or
            board[4] == symbol and board[5] == symbol and board[6] == symbol or
            board[7] == symbol and board[8] == symbol and board[9] == symbol or

            board[1] == symbol and board[4] == symbol and board[7] == symbol or
            board[2] == symbol and board[5] == symbol and board[8] == symbol or
            board[3] == symbol and board[6] == symbol and board[9] == symbol or

            board[1] == symbol and board[5] == symbol and board[9] == symbol or
            board[3] == symbol and board[5] == symbol and board[7] == symbol)

