spam = ['apples', 'bananas', 'tofu', 'cats', 'dogs', 'computers', 'chips']
new_string = ''

for i in spam:
    if i == spam[-1]:
        new_string += ('and ' + i)
    else:
        new_string += (i + ", ")


print(new_string)