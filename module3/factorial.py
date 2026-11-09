#Factorial Function Definition
def factorial(n):
    if n==0:
        return 1
    else:
        return factorial(n-1)*n

# Test
def main():
    n=int(input("Enter a Positive Integer:\n"))
    while n<0:
        n=int(input("There is no factorial for Negative, please enter a positive integer:\n"))

    print(str(n)+"!="+str(factorial(n)))  # Recursive function Call

main()      

    