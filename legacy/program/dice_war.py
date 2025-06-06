from utilities import roll, play_again, goose_boast


def play_dice_war():
    print("Welcome to Dice War!")
    cpu_roll = 0
    player_roll = 0

    while cpu_roll == player_roll: #draws aren't allowed
        cpu_roll = roll(1,6)
        player_roll = roll(1,6)


    
    print(f"Goose rolled: {cpu_roll} \nPlayer rolled: {player_roll}\n")
    if player_roll > cpu_roll:
        print("So player wins!")
    elif player_roll < cpu_roll:
        print("So Goose wins!")
        if roll(1,20) == 20: #easter egg. Prints a random boast 
            goose_boast()
 
    if play_again():
        play_dice_war()
