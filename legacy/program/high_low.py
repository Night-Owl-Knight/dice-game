from utilities import roll, play_again


def play_high_low():
    first_roll= roll(1,6)
    second_roll = roll(1,6)
    
    while True: #loops until player makes a valid input
     
        print("Welcome to High/Low!")
        print("Will the next roll be higher (1), lower(2), or equal(3) to ", first_roll)

        player_guess = input("").strip()
        if player_guess in ['1','2','3']:
            break 
        else:
            print("Invalid input. Please try again.")

    print(f"Next roll was {second_roll}, so")
    if (first_roll == second_roll and player_guess == '3') or \
        (first_roll > second_roll and player_guess == '2') or \
        (first_roll < second_roll and player_guess == '1'):
        print("You are correct!")
    
    else:
        print("You are incorrect!")

    if play_again():
        play_high_low()