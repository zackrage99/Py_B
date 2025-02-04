""" Game where each user take a turn and gamble a number
each number is added to his score as long as it not randomly appears number 1
all is score is set to zero"""
import random
def value_generator():
    """ Function for generating random numbers"""
    rolled_value=random.randint(1,6)
    return rolled_value
# Taking number of players
while True:
    print("Enter how many players (2-4): ")
    players=input()
    if players.isdigit():
        players=int(players)
        if 2<=players<=4:
            break
        else:
            print("Only allowed 2-4 !")
    else:
        print("Enter only numbers.")
max_score=50
players_score=[0 for _ in range(players)]
while max(players_score) < max_score:
    for index_player in range(players):
        print(f"Player {index_player+1} has just started!")
        current_score=0
        while True:
            print("Do you want to roll (Y): ")
            want_roll=input().lower()
            if want_roll != 'y':
                break
            value=value_generator()
            if value== 1:
                print("You rolled a 1 turn out!")
                current_score=0
                break
            else:
                current_score=current_score+value
                print(f"You rolled a {value}")
        players_score[index_player]+=current_score
        print(f"Your total score is {players_score[index_player]}")
max_player=max(players_score)
winning_idx=players_score.index(max_player)
print(f"The winner is {winning_idx+1} whith a score of {max_player}")
