import random

# Define the binary search function
def binarySearch(arr, target, low, high):
    # If there are no more elements to search, return -1
    if low > high:
        return -1

    # Find the middle position
    mid = (low + high) // 2

    # If the middle element is the target, return its position
    if arr[mid] == target:
        return mid

    # If the target is smaller, search the first half
    elif target < arr[mid]:
        return binarySearch(arr, target, low, mid - 1)

    # If the target is larger, search the second half
    else:
        return binarySearch(arr, target, mid + 1, high)


def main():
    # Create a list of 10 random numbers from 1 to 100
    numbers = random.sample(range(1, 101), 10)

    # Sort the list in ascending order for binary search
    numbers.sort()

    # Display the random list
    print("The list of 10 random numbers is:")
    print(numbers)

    # Keep asking the user for a number until they enter q
    while True:
        user_input = input("Enter a number to search for, or enter 'q' to quit:\n")

        # Quit the program if the user enters q
        if user_input.lower() == "q":
            break

        # Convert the input to an integer
        target = int(user_input)

        # Call the recursive binary search function
        result = binarySearch(numbers, target, 0, len(numbers) - 1)

        # Check if the number was found
        if result == -1:
            print(target, "Not found!!")
        else:
            print(target, "Found at position", result)

    # Display the ending message
    print("Program Ended!")


# Run the main function
main()