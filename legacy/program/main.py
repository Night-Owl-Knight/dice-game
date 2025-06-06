#Date: 5/08/2025
#Program Purpose: This is a collection of several dice based mini-games (High or low, Dice War, Goose's Gambit)
# with a handful of goose-based easter eggs




from utilities import show_instructions, roll, goose_boast
from high_low import play_high_low
from dice_war import play_dice_war
from dice_poker import play_poker



def exit_game(): #ends program and prints thank you message
    print("Thanks for playing!")
    exit()


goose = False # activates an easter egg if it becomes true

def main(): #displays the main menu
 
 menu_options = {
    "1": play_high_low,
    "2": play_dice_war,
    "3": play_poker,
    "4": show_instructions,
    "5": None, # slightly jank way of calling a dice roll, but it works
    "6": exit_game

}
 

 while True: 
    global goose
    print("1. High or Low\n2. Dice War\n3. Goose's Gambit\n4. How to play\n5. Dice Roll\n6. Exit Game")
    try: #start of try block
     if not goose:
      choice = input("Choose which game to play (1-6): ")
     if goose: # rolls a random number on the main menu. It can quit the game if it rolls high
      choice = str(roll(1,6))
      if choice == '6':
        print("Goose has ended the game.")
     goose = False # resets so it only randomizes once

     if choice in menu_options and choice != '5':
       menu_options[choice]()
     elif choice == '5':
       print(f"You rolled a {roll(1,6)}.") # just rolls one number
     elif choice.lower() in {'honk', 'honk!'}: #easter egg
       print("Goose will decide your fate!")
       print(goose_boast())
       goose = True
       choice = roll(1, 6)
       main()
     else:
      print("Invalid option. Please try again.")
    except Exception as e: # end of try block. I can't see any way there could be an exception, but it's here just in case
      print("An unexpected error occurred: ", e)


main()
