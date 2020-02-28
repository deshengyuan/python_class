# Pseudocode
# Create a variable called board initialized as dictionary with 9 keys 1-9
# Create a variable called active, set it true
# Create a variable called current_player, set it to 'X'
# Create a variable called next_player, set it to 'O'
# While active is ture
  # print the board
  # create a variable called vaild_move, set it to false
  # ask current player to pick a move
  # if move is vaild 
  # update the board (set key at input ro current_player)
  # set vaild_move to true
  # if player has won --print message, set active to false
  # else if the board is full--print message, set active to false
  # else switch current player and next player



SPACES=list('123456789')
game_board={}
for s in SPACES:
  game_board[s]=" "




def print_board(b):
  print(f'''
    {b['1']} | {b['2']} | {b['3']}  1 2 3
    --+---+--
    {b['4']} | {b['5']} | {b['6']}  4 5 6
    --+---+--
    {b['7']} | {b['8']} | {b['9']}  7 8 9

   ''')
# print_board(game_board)

# game_board['1']='X'
# game_board['5']='O'
# print(game_board)
# print_board(game_board)


def check_winner(b, player):
  return ((b['7'] == b['8'] ==b['9'] == player) or 
         (b['4'] == b['5'] == b['6'] == player) or 
         (b['1'] == b['2'] == b['3'] == player) or 
         (b['7'] == b['4'] == b['1'] == player) or 
         (b['8'] == b['5'] == b['2'] == player) or 
         (b['9'] == b['6'] == b['3'] == player) or 
         (b['7'] == b['5'] == b['3'] == player) or 
         (b['9'] == b['5'] == b['1'] == player) 
         )   




def check_has_availble_empty(b):
  return ' 'in b.values()



active =True
current_player ="X"
next_player ="O"
SPACES = list('123456789')
game_board ={}
for s in SPACES:
    game_board[s] =" "

while active:
    print_board(game_board)
    waiting_for_vaild_input = True
    while waiting_for_vaild_input:
        space= input(f"{current_player}'s move\n Please enter a space 1-9 \n")
        if space in SPACES and game_board[space] == " ":
            game_board[space] = current_player
            waiting_for_vaild_input = False
        else:
            print(" Sorry, that's not a vaild space. Please try again.")

    if check_winner(game_board,current_player):
            print(f"yay!{current_player} WINS!")
            active= False
    elif not ' ' in game_board.values():
            print("Scratch Game!")
            print_board(game_board)
            active =False
    else:
         current_player, next_player = next_player,current_player

