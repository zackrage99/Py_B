""" Roll dice program asks the user how many times to roll and roll"""
import random
tracker=0
# Main program loop
while True:
    print("Roll the dice? (y/n): ")
    choice=input()
    if choice.lower() == 'y':
        print("Choose how many dices to roll? ")
        try:
            how_many=int(input())
            # Adding number of rolled dices each time the user play
            tracker=tracker+how_many
            # Looping through number of times
            for number in range(how_many):
                roll_dice1=random.randint(1,6)
                roll_dice2=random.randint(1,6)
                print(f'({roll_dice1},{roll_dice2})')
            print(f"You have rolled the dice {tracker} times.")
        except ValueError:
            print("Invalid Input.")
    elif choice.lower() == 'n' :
        print("Thank you for playing.")
        break
    else:
        print("Invalid choice!")
