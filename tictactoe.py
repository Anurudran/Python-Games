BOARD = {1: '1',  2: '2',  3: '3',

        4: '4',  5: '5',  6: '6',

        7: '7',  8: '8',  9: '9'}

playerX_score = 0
playerO_score = 0
draw_score = 0


def render():
    '''
    Returns a string describing the board in its
    current state. It should look something like this:

     1 | 2 | 3
     - + - + -
     4 | 5 | 6
     - + - + -
     7 | 8 | 9

    Returns
    -------
    board_state : str

    Implements (See also)
    ---------------------
    BOARD : dict
    '''

    board_state = ""
    for i, key in enumerate(BOARD):
        if i == 2 or i == 5:
            board_state += f" {BOARD[key]} \n - + - + - \n"
        elif i == 8:
            board_state += f" {BOARD[key]}"
        else:
            board_state += f" {BOARD[key]} |"
    return board_state


def get_action(player):
    '''
    Prompts the current player for a number between 1 and 9.
    Checks* the returning input to ensure that it is an integer
    between 1 and 9 AND that the chosen board space is empty.

    Parameters
    ----------
    player : str

    Returns
    -------
    action : int

    Raises
    ======
    ValueError, TypeError

    Implements (See also)
    ---------------------
    BOARD : dict

    *Note: Implementing a while loop in this function is recommended,
    but make sure you aren't coding any infinite loops.
    '''


    while True:
        try:
            num = int(input("Pick a number on the board: "))
        except ValueError or TypeError:
            print("Input must be an integer")
        else:
            if 1 <= num <= 9 and BOARD[num] == str(num):
                return num
            else:
                print("Enter integer from 1 to 9 or integer that isnt used")


def victory_message(player):
    '''
    Prints the updated board and returns a victory message for the
    winning player.

    Parameters
    ----------
    player : 'X' / 'O'

    Returns
    -------
    victory_message : str

    Implements (See also)
    ---------------------
    print_t3() : func
    '''

    print(render())
    if player == "X":
        global playerX_score
        playerX_score += 1
    else:
        global playerO_score
        playerO_score += 1
    msg = f"The winner of this TicTacToe game is player {player}: Player X score is {playerX_score}, Player O score is {playerO_score}, and draws is {draw_score}"
    with open('game_history.txt', 'a') as file:
        file.write(f"{msg}\n")
    print(msg)



def check_win(player):
    '''
    Checks victory conditions. If found, calls victory_message().
    This can be done with one long chain of if/elif statements, but
    it can also be condensed into a single if/else statement, among
    other strategies (pattern matching if you have python 3.10 or above).

    Parameters
    ----------
    player : 'X' / 'O'

    Returns
    -------
    True or False : bool

    Implements (See also)
    ---------------------
    BOARD : dict
    victory_message(player) : func
    '''

    # Check rows
    if BOARD[1] == player and BOARD[2] == player and BOARD[3] == player:
        victory_message(player)
        return True
    elif BOARD[4] == player and BOARD[5] == player and BOARD[6] == player:
        victory_message(player)
        return True
    elif BOARD[7] == player and BOARD[8] == player and BOARD[9] == player:
        victory_message(player)
        return True
    
    #Check coloumns
    elif BOARD[1] == player and BOARD[4] == player and BOARD[7] == player:
        victory_message(player)
        return True
    elif BOARD[2] == player and BOARD[5] == player and BOARD[8] == player:
        victory_message(player)
        return True
    elif BOARD[3] == player and BOARD[6] == player and BOARD[9] == player:
        victory_message(player)
        return True

    # Check Diagonals
    elif BOARD[1] == player and BOARD[5] == player and BOARD[9] == player:
        victory_message(player)
        return True
    elif BOARD[3] == player and BOARD[5] == player and BOARD[7] == player:
        victory_message(player)
        return True
    else:
        return False


def play_t3():
    '''
    This is the main game loop that is called from the launcher (main.py)

    Implements (See also)
    ---------------------
    BOARD : dict
    render() : func
    get_action(player) : func
    check_win(player) : func
    play_t3()* : func

    *Note: this function refers to itself. Be careful about
    inescapable infinite loops.
    '''

    player = 'X'
    game_round = 0
    game_over = False

    while not game_over:

        # Print the current state of the board
        print(render())
        # Get the current player's action and assign it to a variable called 'action'.
        action = get_action(player)
        # Assign the current player ('X' or 'O') as a value to BOARD. Use the 'action' variable as the key.
        BOARD[action] = player
        # Increment the game round by 1.
        game_round += 1
        # Check if the game is winnable (game_round >= 4),
        if game_round >= 4:
            # then check for win conditions (check_win(player)),
            if check_win(player):
                # and if there's a win, end the game (game_over = True),
                # and break the loop (break).
                game_over = True
                break

        # Check if there are any open spots left (game_round == 9),
        if game_round == 9:
            # and if there aren't, print a tie message,
            # end the game,
            # and break the loop.
            print("Tie game -_-")
            global draw_score
            draw_score += 1
            msg = f"It was a draw for this tictactoe game: Player X score is {playerX_score}, Player O score is {playerO_score}, and draws is {draw_score}"
            with open('game_history.txt', 'a') as file:
                file.write(f"{msg}\n")
            game_over = True
            break

        # switch players with a quick conditional loop.
        if player == "X":
            player = "O"
        else:
            player = "X"


    # prompt for a restart and assign the input to a 'restart' variable.
    restart = input("Do you want to restart the game (yes/no): ")
    # if yes,
    # clear each key in the board with a for loop
    for i, key in enumerate(BOARD):
        BOARD[key] = str(i+1)
    if restart == "yes":
        # and reinitiate the game loop (play_t3()).
        play_t3()