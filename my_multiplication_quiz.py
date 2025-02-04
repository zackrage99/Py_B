import pyinputplus as py , time , random
numbers_of_questions=10
correct_answers=0
for question in range(numbers_of_questions):
    number1=random.randint(0,9)
    number2=random.randint(0,9)
    display="%s] %s * %s: " %(str(question+1),number1,number2)
    try:
        py.inputStr(prompt=display,allowRegexes=["^%s$" %(number1*number2)],blockRegexes=[('.*',"Incorrect!")],timeout=8,limit=3)
    except py.TimeoutException:
        print("Time out!")
    except py.RetryLimitException:
        print("Out of limits!")
    else:
        print("Correct!")
        correct_answers+=1
        time.sleep(1)
    print("Score: %s / %s : " %(correct_answers,numbers_of_questions))
    print("Do you want to play again? (Y/N): ")
    user_input=input().lower()
    if user_input =='y':
        continue
    elif user_input =='n':
        break
    else:
        print("Invalid input.")
