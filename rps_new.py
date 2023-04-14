import random

final_p1_score, final_comp_score, final_p2_score, final_draw_score = 0, 0, 0, 0
def rps():
# Moves for rock, paper and scissors
    moves = ['r', 'p', 's']

    print("We about to play Rock Paper Scissors!")
    while True:
    # This is to ask user whether to play with a computer or another player
        opponent = input("""
Choose your opponent:
1: Computer
2: Another player
""")
        if opponent == "1":
            opponent = "Computer"
            break
        elif opponent == "2":
            opponent = "Player 2"
            break
        else:
            print("Choose the input properly")
        

    # Tracker of wins
    global final_p1_score, final_comp_score, final_p2_score, final_draw_score
    p1_score, comp_score, draw_score, p2_score = 0,0,0,0

    rounds = ["0", "3", "5"]

    scenario = input("Pick number of rounds: 0 (infinite), 3, or 5: ")

    # Goes through a loop to see which game mode the user chooses
    while scenario not in rounds:
        print("Pick a correct game mode")
        scenario = input("Pick number of rounds: 0 (infinite), 3, 5 ")

    while True:
        #Change the rounds to an int
        r = int(scenario)
        # Player 1 moves
        p1 = input("What is your move? (only say r, p or s for rock, paper or scissors\n").lower()
        # Keep on asking Player 1 to make a correct move
        while p1 not in moves:
            print("Wrong move, choose only r, p, or s")
            p1 = input("Player 1: What is your move? (only say r, p or s for rock, paper or scissors\n").lower()
        
        if opponent == "Computer":
            # Computer chooses a move
            comp = random.choice(moves)
        else:
            comp = input("What is your move? (only say r, p or s for rock, paper or scissors\n").lower()
            while comp not in moves:
                print("Wrong move, choose only r, p, or s")
                comp = input("Player 2: What is your move? (only say r, p or s for rock, paper or scissors\n").lower()

        # Both choose same move
        if p1 == comp:
            print("Tie game!")
            draw_score += 1

        # Player 1 makes the better move
        elif (p1 == "r" and comp  == "s") or (p1 == "p" and comp  == "r") or (p1 == "s" and comp  == "p"):
            print("Player 1 wins!")
            p1_score += 1

        # Computer makes the better move
        else:
            print(f"{opponent} wins!")
            if opponent == "Computer":
                comp_score += 1
            else:
                p2_score += 1
        if opponent == "Computer":    
            if r == comp_score + p1_score + draw_score:
                break
        else:
            if r == p2_score + p1_score + draw_score:
                break
        if r == 0:
            flag = input("Do you want to quit or no, type y or n\n")
            if flag == "y":
                break
        
    print(f"Game score are you is: {p1_score}, {opponent} score is: {comp_score}, draws is {draw_score}")
    if opponent == "Computer":
        if p1_score > comp_score:
            print("YOU WIN :)")
            final_p1_score +=1
        elif p1_score < comp_score:
            print("You lose :(")
            final_comp_score += 1
        else:
            print("Tie game -_-")
            final_draw_score += 1
    else:
        if p1_score > p2_score:
            print("YOU WIN :)")
            final_p1_score += 1
        elif p1_score < p2_score:
            print("You lose :(")
            final_p2_score += 1
        else:
            print("Tie game -_-")
            final_draw_score += 1
    msg = f"Rock Paper Scissors Game: The final overall score for this game is you have {final_p1_score} points, player 2 has {final_p2_score} points and computer has {final_comp_score} points and draws are {final_draw_score}"
    with open('game_history.txt', 'a') as file:
        file.write(f"{msg}\n")

