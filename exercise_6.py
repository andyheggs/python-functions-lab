# Exercise 6: Find the Largest Number
#
# Write a function named `largest` that takes three integers as arguments and returns the largest of them.
#
# Examples:
# largest(1, 2, 3) should return 3.
# largest(10, 4, 2) should return 10.
#
# Define your function and test it with different inputs.

def largest(n, o, p):

    if n > o and n > p:

        return n
    
    elif o > n and o > p:

        return o

    else: 

        return p 

print('Exercise 6:', largest(10, 4, 2))

# alternate syntax 

def largest(n, o, p):

    return max(n, o, p)

print('Exercise 6:', largest(10, 4, 2))