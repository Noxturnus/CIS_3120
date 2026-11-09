#Cis 3120 Exam 1 Recursive Merge Sort
def merge_sort(arr):
    # Base Case
    if len(arr) <= 1:
        return arr

    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

    #print the divide of the array into two halves
        print("Divide:", arr, "to", left_half, right_half)
    
    # Recursive call on each half
    L = merge_sort(left_half)

    R = merge_sort(right_half)

    return merge(L, R)

#define the merge function to merge two lists into one list
def merge(left, right): 
    merged = []
    i, o = 0, 0

#do while loop to merge the two lists
    while i < len(left) and o < len(right):
        if left[i] < right[o]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[o])
            o += 1

#append the remaining elements of the left and right lists to the merged list
    merged.extend(left[i:])
    merged.extend(right[o:])

    print("Merge:", left, right, "to", merged)

    return merged

#set the input list and print the input and output of the merge_sort function
numbers = [9, 8, 7, 6]
print("Input:", numbers)
print("Output:", merge_sort(numbers))
