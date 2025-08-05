import random

def dice_game():
    print("Welcome to the Dice Roll Challenge!")
    print("Roll higher than the computer to win!")
    
    player_score = 0
    computer_score = 0
    
    while True:
        input("\nPress Enter to roll (or 'quit' to exit)... ")
        
        # Player rolls
        player_roll = random.randint(1, 6)
        print(f"\nYou rolled: {player_roll}")
        
        # Computer rolls
        computer_roll = random.randint(1, 6)
        print(f"Computer rolled: {computer_roll}")
        
        # Determine winner
        if player_roll > computer_roll:
            print("You win this round!")
            player_score += 1
        elif computer_roll > player_roll:
            print("Computer wins this round!")
            computer_score += 1
        else:
            print("It's a tie!")
        
        print(f"Score - You: {player_score}  Computer: {computer_score}")
        
        # Ask to continue
        choice = input("\nRoll again? (y/n): ").lower()
        if choice != 'y':
            print("\nFinal Scores:")
            print(f"You: {player_score}  Computer: {computer_score}")
            if player_score > computer_score:
                print("You won the game!")
            elif computer_score > player_score:
                print("Computer won the game!")
            else:
                print("The game ended in a tie!")
            print("Thanks for playing!")
            break

# Start the game
dice_game()
