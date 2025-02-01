''' Number guessing game that keeps track of user input
 and print the score of the user'''
import random
import sys
def main():
    """ MAin Game Loop"""

    limits_list=[]
    while True:
        print("Enter the first number: ")
        num1=input()
        print("Enter the second number: ")
        num2=input()
        limit=0
        try:
            num1=int(num1)
            num2=int(num2)
            # Generate one randome number from user input
            random_num=random.randint(num1,num2)
        except ValueError:
            print("invalid input.")
            continue
        # loop for 10 limits only
        while limit < 10 :
            print("guess the number (Q to exit): ")
            guess=input()
            try:
                guess=int(guess)
                if guess > random_num:
                    print("Too high ! ")
                    limit +=1
                elif guess < random_num:
                    print("Too low ! ")
                    limit+=1
                else:
                    print("congratulations, you gussed the number. ")
                    limits_list.append(limit)
                    break
            except ValueError:
                if guess.lower()=='q':
                    sys.exit()
                print("only numbers.")
        print(f"Youre scores are {limits_list}")
        print(f"Your best score is {min(limits_list)}")

if __name__ == "__main__":
    main()
