"""
The output of this program could look something like this:

Enter number:
3
10
5
16
8
4
2
1

Input Validation

Add try and except statements to the previous project to detect whether the user types in a noninteger string. Normally, the int() function will raise a ValueError error if it is passed a noninteger string, as in int('puppy'). In the except clause, print a message to the user saying they must enter an integer.
"""

#TODO def collatz(number) if number is even, then collatz() should print number // 2 and return this value.
#TODO If number is odd, then collatz() should print and return 3 * number + 1.

def collatz(number):
    while True:
        if number % 2 == 0:
            #number is even.
            print(number)
            number = number // 2
            continue
        elif number % 2 == 1:
            #number is odd
            print(number)
            number = 3 * number + 1
            if number == 4:
                break
            continue


user_number = int(input('Enter number: '))

collatz(user_number)


