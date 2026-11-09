#Plaindrome Loops
myString=input("Enter a String:\n")
start=0
end=len(myString)-1

flag=True

while start<end:
    if myString[start]!=myString[end]:
        flag=False
    start+=1
    end-=1

if flag:
    print("The String",myString,"is a Plaidrome")
else:
    print("The String",myString,"is NOT a Plaidrome")

