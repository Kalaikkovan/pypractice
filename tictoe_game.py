from IPython.display import clear_output
import random

def display_board(board):
    num = 1
    mylist = [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']
    for i in range(len(board)):
        #if num <4:
         mylist[i] = board[i]
        #num +=1
    print(' {}  | {}  | {} '.format(mylist[7],mylist[8],mylist[9]))
    print('\n---------------')
    print(' {}  | {}  | {} '.format(mylist[4],mylist[5],mylist[6]))
    print('\n---------------')
    print(' {}  | {}  | {} '.format(mylist[1],mylist[2],mylist[3]))

def player_input():
    marker = ''
    
    while marker not in ('X','O'):
        marker = input('Would you like to choose "X" or "O" : ' ).upper()
    
    if marker == 'X':
        return ('X','O')
    else: 
        return ('O','X')
    
def place_marker(board, marker, position):
    if space_check(board,position):
        board[position] = marker
    else:
        print('Selected position is already marked')
        player_choice(board)

def win_check(board, mark):
    #result = False
    if ((board[1]==mark and board[2]==mark and board[3]==mark) or
        (board[4]==mark and board[5]==mark and board[6]==mark) or
        (board[7]==mark and board[8]==mark and board[9]==mark) or
        (board[7]==mark and board[4]==mark and board[1]==mark) or
        (board[8]==mark and board[5]==mark and board[2]==mark) or
        (board[9]==mark and board[6]==mark and board[3]==mark) or
        (board[7]==mark and board[5]==mark and board[3]==mark) or
        (board[9]==mark and board[5]==mark and board[1]==mark)):
            return True
    else:
        return False 



def choose_first():
    player_list = ['Player1','Player2']
    choose = random.randrange(0,2)
    player = player_list[choose]
    return player

def space_check(board, position):
    if board[position] not in ['O','X']:
        return True
    else:
        return False

def full_board_check(board):
    for i in board:
        if i not in ['X','O']:
            return False
    return True

def player_choice(board):
    user_choice = 0
    #Print('Hello pl select the next position')
    while user_choice not in range(1,9) or not space_check(board,user_choice):
        user_choice = int(input('Please select the number in range 1 and 9'))
    return user_choice

def replay(str):
    replay_choice = ''
    while replay_choice not in ['Y','N']:
        replay_choice = input('Would you like to play {} Y/N'.format(str))
    return replay_choice

def game():
 
    while True:
        print('Welcome to Tic Tac Toe!')
        theBoard = [' '] * 10
        player = ''
        play_on = replay('')
        if play_on =='Y':
            game_on = True
            player1_marker,player2_marker = player_input()
            player = choose_first()
            print(player + ' will go first')
        else:
            game_on = False
            print('Bye Bye')
            break

        

        while game_on:
        
        
            if player == 'Player1':
                display_board(theBoard)
                position= player_choice(theBoard)
                place_marker(theBoard,player1_marker,position)
                
                if win_check(theBoard,player1_marker):
                    display_board(theBoard)
                    game_on= False
                    print('COngratulations!')
                else:
                    if full_board_check(theBoard):
                        display_board(theBoard)
                        print('Game over - Its draw')
                        break
                    else:
                        player = 'Player2'
            else:
                
                display_board(theBoard)
                position= player_choice(theBoard)
                place_marker(theBoard,player2_marker,position)
                
                if win_check(theBoard,player2_marker):
                    display_board(theBoard)
                    game_on= False
                    print('Congratulations! Player2')
                else:
                    if full_board_check(theBoard):
                        display_board(theBoard)
                        print('Game over - Its draw')
                        break
                    else:
                        player = 'Player1'
                        
                
        if not replay(''):
            break
    
game()
