from utilities import roll, play_again, goose_boast

def play_poker():
    player_hand = []; cpu_hand = []
    print("Welcome to Goose's Gambit!")

    deal(player_hand)
    deal(cpu_hand)

    #scores both players
    player_score = score_hand(player_hand)
    cpu_score = score_hand(cpu_hand)

    print("Your hand is: ", player_hand, "\nSo your score is", player_score, 
          "\nWould you like to roll again? This cannot be undone. y/n")
    roll_again = input()

    if roll_again == 'y' or roll_again == 'yes': #defaults to no
        deal(player_hand)
        player_score = score_hand(player_hand)


    print("Player's hand was: ", player_hand, "\nGoose's hand was: ", cpu_hand)
    print("Therefore:\nPlayer scored: ", player_score, "\nGoose scored: ", cpu_score)

    #determines winner
    if player_score > cpu_score:
        print("Player Wins!")

    elif player_score < cpu_score:
        print("Goose wins!")

        if roll(1, 10) == 10 or cpu_score == 100000:
            goose_boast()
    else:
        print("It was a draw!")

    
    

    if play_again():
        play_poker()


def score_hand(hand):
    score = 0
    dice_count = {}

    for die in hand:
        if die in dice_count:
            dice_count[die] +=1
        else:
            dice_count[die] = 1    
    #check for a straight
    if set(hand) == {1,2,3,4,5,6}:
        return 100000 #auto-win condition
    
    else:
        for value, count in dice_count.items():
            if count == 5: # five of a kind
                score += 10000 * value
            elif count == 4: # four of a kind
                score += 5000 * value
            elif count == 3: # three of a kind
                score += 1000 * value
            elif count == 2: # pairs
                score += 100 * value
        score += max(hand) * 10 #technically redundant, but kept for tradition

        return score

def deal(hand):
     hand.clear() #makes sure hand is empty before dealing
     for i in range(6): #generates hands, alternating between player and Goose, to mimic dealing cards
        hand.append(roll(1,6))
    