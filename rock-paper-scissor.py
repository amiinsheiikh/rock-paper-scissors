import random

user_wins = 0
computer_wins = 0

options = ["rock", "paper", "scissors"]                                         # Possible options to play.

while True:
    user_input = input("Type Rock/Paper/Scissors or Q to quit: ").lower()       # Asking for user input to play
    if user_input == "q":                                                       # quit game if user said Q/q    
        break   

    if user_input not in options:                                               # loops through again if user mispelled a word in input
        continue

    random_number = random.randint(0, 2)                                        # Generating computer input
    # rock: 0, paper: 1, scissors: 2
    computer_pick = options[random_number]                              
    print("Computer picked", computer_pick + ".")

    if user_input == computer_pick:                                             # Base case when both inputs are equal it's a tie
        print("It's a tie, try again!")

    elif user_input == "rock" and computer_pick == "scissors":                  # Rock wins against scissors --> user wins
        print("You won!")
        user_wins += 1

    elif user_input == "scissors" and computer_pick == "paper":                 # scissors wins against paper --> user wins
        print("You won!")
        user_wins += 1
    
    elif user_input == "paper" and computer_pick == "rock":                     # paper wins against rock --> user wins
        print("You won!")
        user_wins += 1

    else:                                                                       # All other cases use loses.
        print("You lost!")
        computer_wins += 1

print("You won", user_wins, "times.")
print("The computer won", computer_wins, "times.")
print("Goodbye!")
