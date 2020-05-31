                                        #Combining Everything 
from IPython.display import clear_output
import random

def display_board(board):
    
    '''
    Display the board
    '''
    
    clear_output()
    print('  |   |')
    print(board[7]+' | '+board[8]+' | '+board[9])
    print('  |   |')
    print ('----------')
    print('  |   |')
    print(board[4]+' | '+board[5]+' | '+board[6])
    print('  |   |')
    print ('----------')
    print('  |   |')
    print(board[1]+' | '+board[2]+' | '+board[3])
    print('  |   |')
    
def player_input():
    
    '''
    Output = (Player 1 marker, Player 2 marker)
    '''
    
    marker= ''
    
    while marker != 'X' and marker!= 'O' :
        marker = input ('Player 1: Choose X or O: ').upper()
        
    if marker == 'X':
        return ('X', 'O')
    else:
        return ('O', 'X')
    
def place_maker(board, marker, position):
    board[position] = marker
    
    
def win_check(board, mark):
    #WIN TIC TAC TOE
    
    return ((board[7] == mark and board[8] == mark and board[9] == mark) or # across the top
    (board[4] == mark and board[5] == mark and board[6] == mark) or # across the middle
    (board[1] == mark and board[2] == mark and board[3] == mark) or # across the bottom
    (board[7] == mark and board[4] == mark and board[1] == mark) or # down the middle
    (board[8] == mark and board[5] == mark and board[2] == mark) or # down the middle
    (board[9] == mark and board[6] == mark and board[3] == mark) or # down the right side
    (board[7] == mark and board[5] == mark and board[3] == mark) or # diagonal
    (board[9] == mark and board[5] == mark and board[1] == mark)) # diagonal

def choose_first():  #Randomly choose which player will go first
    
    flip = random.randint(0,1)
    
    if flip == 0:
        return 'Player 1'
    else:
        return 'Player 2'
    
def space_check(board, position): #Check if specified position is empty on the board
    
    return board[position] == ' '

def full_board_check(board):  #Check if the board is full
    
    for i in range (1, 10):
        if space_check(board, i):
            return False
        
    return True

def player_choice(board):   #Take input of position from the player
    
    position = 0
    
    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board, position):
        position = int(input('Choose a position: (1-9)'))
    return position   

def replay():        #Check if players want to play the game again
    
    choice = input ("Play again ? Enter Yes or No")
    
    return choice == 'Yes'




#WHILE LOOP TO KEEP RUNNING THE GAME 

while True:
    
    #Play the game
    
    ##SET (BOARD, WHOS 1st, CHOOSE MARKER X, O)
    the_board = [' ']*10
    
    player1_marker, player2_marker = player_input()
    
    turn = choose_first()
    print(turn + " will go first")
    
    play_game = input ('Are you ready to Play Y or N')
    
    if play_game == 'y':
        game_on = True
    else:
        game_on = False
        
    ##GAME PLAY
    
    while game_on:
        
        if turn == 'Player 1':
            print ("Player 1teru")
            #show the board
            display_board(the_board)
            #choose a porition
            position = player_choice(the_board)
            #Place the market on the position 
            place_maker(the_board, player1_marker, position)
            
            #Check if they won
            if win_check(the_board, player1_marker):
                display_board(the_board)
                print('Player 1 has WON')
                game_on = False
            else:
                if full_board_check(the_board): #Or check if there is a tie
                    display_board(the_board)
                    print ("The Game is a TIE")
                    game_on = False
                else:
                    turn = 'Player 2'  #No tie and no win? Then next player's turn
                    
                    
            
            
           
    
        ###PLAYER ONE TURN 
        
        else:
            print ("Player 2 turnweh ")
            #show the board
            display_board(the_board)
            #choose a porition
            position = player_choice(the_board)
            #Place the market on the position 
            place_maker(the_board, player2_marker, position)
            
            #Check if they won
            if win_check(the_board, player2_marker):
                display_board(the_board)
                print('Player 2 has WON')
                game_on = False
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print ("The Game is a TIE")
                    game_on = False
                else:
                    turn = 'Player 1'

  
    
    if not replay():
        break
