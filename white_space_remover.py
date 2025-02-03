"""A program that takes the user input and remove all white spaces"""
import re
word=re.compile(r'''(
                (\s+)?        # First white space
                (\s+|\w+) # Words
                (\s+)?       # Second white space
                )''',re.VERBOSE)
print("Enter your word: ")
user_input=input()
words=word.sub(r'\3',user_input)
print(words)
