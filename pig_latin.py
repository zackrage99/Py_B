""" A program takes a word if the first letter is constant it's removed to the end of the word and added ay
if the first letter is vowel way is added to the end of the word"""
import time
vowels=['i','e','o','u','a']
print("========== Welcom to PIG LATIN ==========")
time.sleep(2)
while True:
    print("Enter a word: ")
    user_input=input()
    # Checking if first letter is constant or vowel
    if user_input[0] not in vowels:
        constant=user_input[1:]+user_input[0]+"ay"
        print(f"Your new pig latin word is {constant}")
    else:
        vowel=user_input+"way"
        print(f"Your new pig latin word is {vowel}")
    print("\nDo you to continue playing (N for exit): ")
    user_answer=input().lower()
    if user_answer=='n':
        break
