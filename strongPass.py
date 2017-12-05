'''

Strong Password Detection

Write a function that uses regular expressions to make sure the password string it is passed is strong.
You may need to test the string against multiple regex patterns to validate its strength.

endsWithNumber = re.compile(r'\d$')
endsWithNumber.search('Your number is 42')
<_sre.SRE_Match object; span=(16, 17), match='2'>

endsWithNumber.search('Your number is forty two.') == None
True

'''
import re
def checkPass(pw):
    hasLowercase = re.compile(r'[a-z]')
    hasUppercase = re.compile(r'[A-Z]')
    hasDigit = re.compile(r'\d')

    # 8 characters long.
    if len(pw) < 8:
        print('Password is to short.')
    elif hasLowercase.search(pw) ==  None:
        print('Password is missing a lowercase character')
    elif hasUppercase.search(pw) == None:
        print('Password is missing an Uppercase character')
    elif hasDigit.search(pw) == None:
        print('Password need at least one digit')
    else:
        print('Password is strong')


password = input('Enter Password: ')
checkPass(password)

