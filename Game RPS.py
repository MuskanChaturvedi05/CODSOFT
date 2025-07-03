import random

print("Welcome to the game!")
def rock_paper_scissor():
    print("Choose : Rock/Paper/Scissor?")

    choices = ["rock","paper","scissor"]
    while True:
        player_choice = input("Your choice : ").lower()

        if player_choice not in choices:
            print("Invalid choice! Please choose Rock/Paper/Scissor.")
            continue
        computer_choice = random.choice(choices)

        print(f"Computer chose: {computer_choice}")
         
        if player_choice == computer_choice:
            print("It's a tie!")

        elif (player_choice == "rock" and computer_choice == "scissor") or \
             (player_choice == "paper" and computer_choice == "rock") or \
             (player_choice == "scissor" and computer_choice == "paper"):
              print("You Win!")

        else:
            print("You Lose!")
            
        play_again = input("Do you want to play again?(yes/no): ").lower()
        if play_again != "yes":
            print("Thanks for playing! Goodbye!")
            break

rock_paper_scissor()        