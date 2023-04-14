import random
# Here we implement the game guess game

comp_score = 0
player_score = 0

# Plays game
def play_game():
    random_num = random.randint(1, 100)
    guess = get_difficulty()
    correcly_guessed = False
    global comp_score
    global player_score
    while not correcly_guessed and guess > 0:
        print(f"You have {guess} guess left")
        num = get_user_input()
        guess -= 1
        correcly_guessed = determine_guess(num, random_num)
    if correcly_guessed:
        player_score += 1
        msg = f"Guessing game: Player won :) Scores are: player has {player_score} points, computer has {comp_score} points"
    else:
        print(f"You lost the number to guess was {random_num}")
        comp_score += 1
        msg = f"Guessing game: Computer won :( Scores are: player has {player_score} points, computer has {comp_score} points"
    with open('game_history.txt', 'a') as file:
        file.write(f'{msg}\n')




# This gets the diffculty of the game
def get_difficulty():
    while True:
        difficulty = input("""
Choose your difficulty the range of numbers from 1 to 100:
1: Easy (Guesses: 50)
2: Medium (Guesses: 20)
3: Hard (Guesses: 5)
""")
        if difficulty == "1":
            return 50
        elif difficulty == "2":
            return 20
        elif difficulty == "3":
            return 5
        else:
            print("Pick a correct input")

# This gets user input
def get_user_input():
    while True:
        try:
            num = int(input("Choose a number: "))
            if 1 <= num <= 100:
                return num
            else:
                print("Choose a number from 1 to 100")
        except:
            print("Invalid input choose an integer number")
    

# This determines the logic on whether the user guessed correctly or not
def determine_guess(guess_num, actual_num):
    if guess_num == actual_num:
        print("CONGRATS you guessed the correct number")
        return True
    elif actual_num - 5 <= guess_num <= actual_num + 5:
        print("You are REALLY close to the number")
    elif actual_num - 10 <= guess_num <= actual_num + 10:
        print("You are close to the number")
    else:
        print("You are not even close to the correct number, try a better guess")
    return False

