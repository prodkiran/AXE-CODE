import random

def rock_paper_scissors():
    print("Welcome to Rock, Paper, Scissors!")
    print("Choose one: rock, paper, or scissors")
    print("Type 'quit' to exit the game")
    
    choices = ['rock', 'paper', 'scissors']
    score = {'player': 0, 'computer': 0}
    
    while True:
        player_choice = input("\nYour choice: ").lower()
        
        if player_choice == 'quit':
            print("\nFinal Score:")
            print(f"Player: {score['player']}  Computer: {score['computer']}")
            print("Thanks for playing!")
            break
            
        if player_choice not in choices:
            print("Invalid choice. Please choose rock, paper, or scissors.")
            continue
            
        computer_choice = random.choice(choices)
        print(f"Computer chose: {computer_choice}")
        
        # Determine the winner
        if player_choice == computer_choice:
            print("It's a tie!")
        elif (player_choice == 'rock' and computer_choice == 'scissors') or \
             (player_choice == 'paper' and computer_choice == 'rock') or \
             (player_choice == 'scissors' and computer_choice == 'paper'):
            print("You win!")
            score['player'] += 1
        else:
            print("Computer wins!")
            score['computer'] += 1
            
        print(f"Score - Player: {score['player']}  Computer: {score['computer']}")

# Start the game
rock_paper_scissors()
