# Exercise 9: Basic Calculator
#
# Create a function named `basicCalculator` that takes three arguments: 
# two numbers and a string representing an operation ('add', 'subtract', 'multiply', 'divide'). 
# Perform the provided operation on the two numbers. In operations where the order of numbers is important, 
# treat the first parameter as the first operand and the second parameter as the second operand.
#
# Examples:
# basicCalculator(10, 5, 'subtract') should return 5.
# basicCalculator(10, 5, 'add') should return 15.
# basicCalculator(10, 5, 'multiply') should return 50.
# basicCalculator(10, 5, 'divide') should return 2.
#
# Define the function and then call it below.

def basicCalculator(n1, n2, operation):
        
    if operation == 'add':
        result = n1 + n2
        print(f"Adding {n1} + {n2} = {result}")
        return result
    
    elif operation == 'subtract':
        result = n1 - n2
        print(f"Subtracting {n1} - {n2} = {result}")
        return result
    
    elif operation == 'multiply':
        result = n1 * n2
        print(f"Multiplying {n1} * {n2} = {result}")
        return result
    
    elif operation == 'divide':
        if n2 == 0:
            raise ValueError("Cannot divide by zero.")
        result = n1 / n2
        print(f"Dividing {n1} / {n2} = {result}")
        return result
    
    else:
        raise ValueError(f"Invalid operation '{operation}'. Please choose from 'add', 'subtract', 'multiply', 'divide'.")   

print('Exercise 9 Result:', basicCalculator(10, 5, "subtract"))
