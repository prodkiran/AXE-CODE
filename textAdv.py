import time

def text_adventure():
    print("MYSTERY ISLAND ADVENTURE")
    print("------------------------")
    print("You wake up on a beach, the waves crashing beside you.")
    print("The sun is setting, and you need to find shelter quickly.")
    time.sleep(2)
    
    # Game state
    inventory = []
    health = 100
    has_flashlight = False
    
    # First decision
    while True:
        print("\nWhat do you do?")
        print("1. Walk towards the jungle")
        print("2. Walk along the beach")
        print("3. Check your pockets")
        print("4. Quit game")
        
        choice = input("Enter your choice (1-4): ")
        
        if choice == "1":
            print("\nYou enter the dense jungle. It's dark and humid.")
            jungle_path(inventory, health, has_flashlight)
            break
        elif choice == "2":
            print("\nYou walk along the beach, your feet sinking in the sand.")
            beach_path(inventory, health, has_flashlight)
            break
        elif choice == "3":
            print("\nYou check your pockets and find:")
            if not inventory:
                print("- Nothing but lint")
            else:
                for item in inventory:
                    print(f"- {item}")
            time.sleep(2)
        elif choice == "4":
            print("Thanks for playing!")
            return
        else:
            print("Invalid choice. Try again.")

def jungle_path(inventory, health, has_flashlight):
    print("\nThe jungle is alive with strange sounds.")
    print("You see a faint light in the distance.")
    
    while True:
        print("\nOptions:")
        print("1. Follow the light")
        print("2. Climb a tree to look around")
        print("3. Turn back to the beach")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            print("\nYou find an abandoned campsite with a working flashlight!")
            has_flashlight = True
            inventory.append("Flashlight")
            print("Added Flashlight to your inventory!")
            cave_entrance(inventory, health, has_flashlight)
            break
        elif choice == "2":
            print("\nFrom the tree, you spot a cave entrance to the north.")
            time.sleep(1)
            print("You also see something shiny in a nearby bush.")
            time.sleep(1)
            print("You climb down carefully.")
        elif choice == "3":
            print("\nYou return to the beach.")
            text_adventure()
            return
        else:
            print("Invalid choice.")

def beach_path(inventory, health, has_flashlight):
    print("\nThe beach stretches far in both directions.")
    print("To your left, you see a boat washed ashore.")
    print("To your right, there are strange markings in the sand.")
    
    while True:
        print("\nOptions:")
        print("1. Investigate the boat")
        print("2. Follow the markings")
        print("3. Return to where you woke up")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            print("\nThe boat is damaged beyond repair, but you find a knife!")
            inventory.append("Knife")
            print("Added Knife to your inventory!")
            time.sleep(1)
        elif choice == "2":
            print("\nThe markings lead you to a hidden cave entrance!")
            cave_entrance(inventory, health, has_flashlight)
            break
        elif choice == "3":
            print("\nYou return to where you started.")
            text_adventure()
            return
        else:
            print("Invalid choice.")

def cave_entrance(inventory, health, has_flashlight):
    print("\nYou stand before a dark cave entrance.")
    if has_flashlight:
        print("Your flashlight illuminates the path ahead.")
    else:
        print("It's too dark to see inside without a light source.")
    
    while True:
        print("\nOptions:")
        if has_flashlight:
            print("1. Enter the cave")
        else:
            print("1. Enter the cave (dangerous without light)")
        print("2. Look around the entrance")
        print("3. Leave the cave area")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            if has_flashlight:
                print("\nWith your flashlight, you safely explore the cave...")
                time.sleep(2)
                print("You discover ancient carvings that reveal the island's secret!")
                time.sleep(1)
                print("Congratulations! You've solved the mystery!")
                play_again()
                return
            else:
                print("\nYou stumble in the dark and fall into a pit!")
                health -= 50
                print(f"Ouch! You lose 50 health. Current health: {health}")
                if health <= 0:
                    print("You didn't survive your injuries. Game over!")
                    play_again()
                    return
        elif choice == "2":
            print("\nYou find some edible berries growing nearby.")
            health = min(100, health + 20)
            print(f"You eat some berries and regain 20 health. Current health: {health}")
        elif choice == "3":
            print("\nYou leave the cave area.")
            if "Flashlight" in inventory:
                text_adventure()
                return
            else:
                beach_path(inventory, health, has_flashlight)
                return
        else:
            print("Invalid choice.")

def play_again():
    while True:
        choice = input("\nWould you like to play again? (yes/no): ").lower()
        if choice == "yes":
            text_adventure()
            return
        elif choice == "no":
            print("Thanks for playing!")
            return
        else:
            print("Please enter 'yes' or 'no'.")

# Start the game
text_adventure()
