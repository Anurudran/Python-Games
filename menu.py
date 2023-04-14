import rps_new, guess_game, tictactoe
# This game is to select the game the user wants

print("----------------------Main Menu---------------------------------")
with open('game_history.txt', 'a') as file:
    file.write('----------------------------New Game History-------------------------------\n')

games = ["1", "2", "3", "exit"]
while True:
    print("""
Your game library:
1: Tic-Tac-Toe
2: Rock Paper Scissors
3: Guessing Game
    """)
    game_choice = input("What game would you like to play? Input the game ID, or type 'exit' to exit.\n")
    if game_choice == "1":
        tictactoe.play_t3()
    elif game_choice == "2":
        rps_new.rps()
    elif game_choice == "3":
        guess_game.play_game()
    elif game_choice == "exit":
        break
    else:
        print("You have selected an incorrect game. Choose a game that you are given\n")
