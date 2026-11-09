# Define a recursive function to reverse a string
def reverse_string(text):

    # base case
    if len(text) <= 1:
        return text

    # Recursive case
    return reverse_string(text[1:]) + text[0]


# Define a recursive function to compute Fibonacci number
def fibonacci(n):

    # base case
    if n == 0:
        return 0
    elif n == 1:
        return 1

    # Recursive case
    return fibonacci(n - 1) + fibonacci(n - 2)

# Define a recursive function for multiplication
def multiply(x, y):

    # base case
    if y == 0:
        return 0

    # Recursive case
    return x + multiply(x, y - 1)


# Test the reveser string, fibonacci, and multiply functions.
def main():

    # Test reverse string
    myString = input("Enter a String:\n")
    print("The reversed String is:", reverse_string(myString))

    print()

    # Test fibonacci
    n = int(input("Enter an integer for Fibonacci:\n"))
    print("The Fibonacci number is:", fibonacci(n))

    print()

    # Test multiply
    x = int(input("Enter the first positive integer:\n"))
    y = int(input("Enter the second positive integer:\n"))
    print("The multiplication result is:", multiply(x, y))

main()