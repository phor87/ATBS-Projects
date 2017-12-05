'''
Regex Version of strip()

Write a function that takes a string and does the same thing as the strip() string method.
If no other arguments are passed other than the string to strip,
then whitespace characters will be removed from the beginning and end of the string.
Otherwise, the characters specified in the second argument to the function will be removed from the string.

namesRegex = re.compile(r'Agent \w+')
namesRegex.sub('CENSORED', 'Agent Alice gave the secret documents to Agent Bob.')
CENSORED gave the secret documents to CENSORED.'
'''

import re

def newF(arg1, arg2):
    aRegex = re.compile(arg2)
    new_sub = aRegex.sub('', arg1)
    print(new_sub)

newF('Agent Alice gave the secret documents to Agent Bob.', 'Agent \w+')