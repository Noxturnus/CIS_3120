#Palindrome Recursion
#Define a recursive function to check
def is_palindrome(text):
    #base case
    if len(text)<=1:
        return True
    #Recursive case
    if text[0]==text[-1]:
        return is_palindrome(text[1:-1]) # recursive call
    else:
        return False

#Test
def main():    
    myString=input("Enter a String:\n")
    if is_palindrome(myString):
        print("The String",myString,"is a Palindrome")
    else:
        print("The String",myString,"is NOT a Palindrome")

main()        

