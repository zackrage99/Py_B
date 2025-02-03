"""A program that takes input from the clipboard and return
    all emails and phone numbers found when pasting using the regular exrepssion """
import re
import pyperclip
phone_regex=re.compile(r'''(
                       (\d{3}|\(\d}3\))?         #area code
                       (\s|-|\.)?                     #spereator
                       (\d{3})                        #first 3 digits
                       (\s|-|\.)                      #seperator
                       (\d{4})                        #last 4 digits  
                       (\s*(ext|x|ext.)\s*(\d{2,5}))? #extension
                    )''',re.VERBOSE)
#Create email regex
email_regex=re.compile(r'''(
                       [a-zA-Z0-9\._%+-]+   # username
                       @                    # @ symbol
                       [a-zA-z0-9]+         # domain name
                       (\.[a-zA-z]{2,4})
                       )''',re.VERBOSE)
#Find matches in clipboard text
text=str(pyperclip.paste())
matches=[]
for group in phone_regex.findall(text):
    phone_num='-'.join([group[1],group[3],group[5]])
    if  group[8] !='':
        phone_num+=phone_num +' x'+group[8]
    matches.append(phone_num)
for groups in email_regex.findall(text):
    matches.append(groups[0])

#copy results to clipboard
if len(matches) >0:
    pyperclip.copy('\n'.join(matches))
    print('Copied to cilpboard: ')
    print('\n'.join(matches))
else:
    print('No phone numbers or email addresses found.')
