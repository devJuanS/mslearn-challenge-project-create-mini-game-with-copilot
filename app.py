import random

continue_game  = True
options        = ['rock', 'paper', 'scissor']
player_score   = 0
computer_score = 0

while continue_game:
    computer_choice = random.choice( options )
    player_choice   = input("Enter your choice (rock, paper, or scissor): ").lower()

    if player_choice == "rock":
        if computer_choice == "rock":
            print("It's a tie! You chose rock and Computer chose rock.")
        elif computer_choice == "paper":
            print("You lost! You chose rock and Computer chose paper.")
            computer_score += 1
        elif computer_choice == "scissor":
            print("You win! You chose rock and Computer chose scissor.")
            player_score += 1
    
    elif player_choice == "paper":
        if computer_choice == "rock":
            print("You win! You chose paper and Computer chose rock.")
            player_score += 1
        elif computer_choice == "paper":
            print("It's a tie! You chose paper and Computer chose paper.")
        elif computer_choice == "scissor":
            print("You lost! You chose paper and Computer chose scissor.")
            computer_score += 1

    elif player_choice == "scissor":
        if computer_choice == "rock":
            print("You lost! You chose scissor and Computer chose rock.")
            computer_score += 1
        elif computer_choice == "paper":
            print("You win! You chose scissor and Computer chose paper.")
            player_score += 1
        elif computer_choice == "scissor":
            print("It's a tie! You chose scissor and Computer chose scissor.")
    else:
        print("The entered option is not valid.")
        break

    play_again = input("Do you want to play again again? [Y/n]: ").lower()
    if play_again != "y":
        print(f"The final score is: You { player_score } vs Computer { computer_score }")
        continue_game = False
