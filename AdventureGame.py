inventory = []
import random
from colorama import init, Fore, Style

init()

TITLE_ART = '''
    🏰 ADVENTURE GAME 🏰
    =================='''

DRAGON_ART = '''
      /\    /\\
     /  \  /  \\
    |    \/    |
  --|----||----|--
     \  /\  /           
      \/  \/'''

LIBRARY_ART = '''
    📚 _________
      |       |
      |       |
      |_______|'''

def start_game():
    print(Fore.CYAN + TITLE_ART + Style.RESET_ALL)
    print(Fore.YELLOW + "\nWelcome to the Adventure Game!" + Style.RESET_ALL)
    print("You find yourself in a " + Fore.CYAN + "Mysterious Chamber" + Style.RESET_ALL + " filled with ancient artifacts.")
    print("\nThere are doors leading to the " + Fore.RED + "Dragon's Lair" + Style.RESET_ALL + 
          " and the " + Fore.BLUE + "Ancient Library" + Style.RESET_ALL + "...")
    room_choice()

def room_choice():
    print("\n" + Fore.GREEN + "Available Locations:" + Style.RESET_ALL)
    print("1. Dragon's Lair")
    print("2. Ancient Library")
    print("3. Garden")
    print("4. Dungeon")
    print("5. Random")
    
    choice = input("\nEnter number (1-5) or location name: ").strip().lower()

    if choice == "5" or choice == "random":
        choice = random.choice(["1", "2", "3", "4"])
    
    if choice in ["1", "dragon's lair", "dragons lair"]:
        dragon_lair()
    elif choice in ["2", "ancient library"]:
        ancient_library()
    elif choice in ["3", "garden"]:
        enchanted_garden()
    elif choice in ["4", "dungeon"]:
        echoing_dungeon()
    else:
        print(Fore.RED + "Invalid choice! Please enter a number (1-5) or location name." + Style.RESET_ALL)
        room_choice()

def dragon_lair():
    print(Fore.RED + DRAGON_ART + Style.RESET_ALL)
    if "sword" in inventory:
        print(Fore.YELLOW + "\nYou enter the Dragon's Lair! The dragon is here!" + Style.RESET_ALL)
        choice = input("\nDo you want to " + Fore.GREEN + "(fight/run)" + Style.RESET_ALL + ": ").strip().lower()
        
        if choice == "fight":
            print(Fore.GREEN + "\n🗡️  You bravely fight the dragon with your sword and win! You take the treasure and escape.")
            print("🏆 Congratulations! You've won the game!" + Style.RESET_ALL)
        elif choice == "run":
            print("You run back to the Mysterious Chamber.")
            room_choice()
        else:
            print("Invalid choice! Please choose fight or run.")
            dragon_lair()
    else:
        print("You cannot fight the dragon without a sword. You must explore the other areas first.")
        room_choice()

def ancient_library():
    print(Fore.BLUE + LIBRARY_ART + Style.RESET_ALL)
    print("You enter the Ancient Library filled with ancient books.")
    print("\nOptions:")
    print("1. Read")
    print("2. Leave")
    choice = input("Enter number (1-2) or action: ").strip().lower()
    
    if choice in ["1", "read"]:
        print(Fore.YELLOW + "You find a book that grants you wisdom. You feel smarter!" + Style.RESET_ALL)
        print("You can now return to the Mysterious Chamber or explore the Enchanted Garden or Echoing Dungeon.")
        room_choice()
    elif choice in ["2", "leave"]:
        print("You leave the Ancient Library and return to the Mysterious Chamber.")
        room_choice()
    else:
        print(Fore.RED + "Invalid choice! Please enter 1 or 2." + Style.RESET_ALL)
        ancient_library()

def enchanted_garden():
    print("You step into the Enchanted Garden filled with flowers.")
    print("\nOptions:")
    print("1. Explore")
    print("2. Return")
    choice = input("Enter number (1-2) or action: ").strip().lower()
    
    if choice in ["1", "explore"]:
        print(Fore.GREEN + "You find a hidden path leading to a sword!" + Style.RESET_ALL)
        inventory.append("sword")
        print(Fore.YELLOW + "You've collected a sword! 🗡️" + Style.RESET_ALL)
        print("You can now return to the Mysterious Chamber or explore the Echoing Dungeon.")
        room_choice()
    elif choice in ["2", "return"]:
        room_choice()
    else:
        print(Fore.RED + "Invalid choice! Please enter 1 or 2." + Style.RESET_ALL)
        enchanted_garden()

def echoing_dungeon():
    print("You enter the Echoing Dungeon filled with echoes.")
    print("\nOptions:")
    print("1. Search")
    print("2. Escape")
    choice = input("Enter number (1-2) or action: ").strip().lower()
    
    if choice in ["1", "search"]:
        print(Fore.YELLOW + "You find a hidden treasure in the Echoing Dungeon! 💎" + Style.RESET_ALL)
        print("You can now return to the Mysterious Chamber.")
        room_choice()
    elif choice in ["2", "escape"]:
        print("You escape back to the Mysterious Chamber.")
        room_choice()
    else:
        print(Fore.RED + "Invalid choice! Please enter 1 or 2." + Style.RESET_ALL)
        echoing_dungeon()

if __name__ == "__main__":
    start_game()
