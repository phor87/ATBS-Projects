"""

  Collatz sequence, sometimes called “the simplest impossible math problem.”)

Remember to convert the return value from input() to an integer with the int() function; otherwise, it will be a string value.

Hint: An integer number is even if number % 2 == 0, and it’s odd if number % 2 == 1.

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