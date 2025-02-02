""" Rock Paper Scissors game where taking user input and play againt the computer"""
import random
import time
user_win=0
computer_win=0
ties=0
over_all_user=0
over_all_computer=0
over_all_losses_user=0
over_all_losses_pc=0
# Main game loop
print("==========Rock Paper Scissor game==========")
time.sleep(2)
print("The first one who wins 3 rounds gets plus one score.\n\n")
while True:
    print("Choose Rock,Paper,Scissors (R/P/S):")
    user_choice=input()
    if user_choice.lower() == 'r':
        chosen='rock'
    elif user_choice.lower() == 'p':
        chosen='paper'
    elif user_choice.lower() == 's':
        chosen='scissors'
    else:
        print("Invalid input.")
        continue
    # Taking random choice from the pc usin random module
    random_choice=random.randint(1,3)
    if random_choice == 1:
        option='rock'
    elif random_choice == 2:
        option ='paper'
    else:
        option = 'scissors'
    while True:
        if chosen =='rock' and option =='scissors':
            print("You win!")
            print(f"Computer chose {option}")
            user_win+=1
        elif chosen =='paper' and option =='rock':
            print("You win!")
            print(f"Computer chose {option}")
            user_win+=1
        elif chosen =='scissors' and option =='paper':
            print("You win!")
            print(f"Computer chose {option}")
            user_win+=1
        elif chosen =='rock' and option =='paper':
            print("You loose!")
            print(f"Computer chose {option}")
            computer_win+=1
        elif chosen =='paper' and option =='scissors':
            print("You loose!")
            print(f"Computer chose {option}")
            computer_win+=1
        elif chosen =='scissors' and option =='rock':
            print("You loose!")
            print(f"Computer chose {option}")
            computer_win+=1
        elif chosen =='paper' and option=='paper':
            print("Tie!")
            print(f"You both chose {option}")
            ties+=1
        elif chosen =='rock' and option=='rock':
            print("Tie!")
            print(f"You both chose {option}")
            ties+=1
        elif chosen =='scissors' and option=='scissors':
            print("Tie!")
            print(f"You both chose {option}")
            ties+=1
            # The first one wins on the first 3 wins is declared the round winner
        if user_win==3:
            over_all_user+=1
            over_all_losses_pc+=1
            continue
        if computer_win == 3:
            over_all_computer+=1
            over_all_losses_user+=1
            continue
        print("Do you want to play again? (Y/N):\nOr (S) for game statistics. ")
        repeat=input()
        if repeat.lower() =='y':
            break
        elif repeat.lower()=='s':
            print(f"\n\nGame statistics:\nUser Wins: {over_all_user}\n\
User Losses: {over_all_losses_user}\n==========================\n\
Computer Wins: {over_all_computer}\n\
Computer Losses: {over_all_losses_pc}\n\
Ties: {ties}")
        elif repeat.lower()=='n':
            quit()
        else:
            print("Please enter only yes or no (Y/N).")
