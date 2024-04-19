num=int(input("Enter a Value"))
temp=num
rev=0
while(num>0):
    dig=num%10
    rev=rev*10+dig
    num=num//10
print(f"The reverse of the number is:{rev}")
if(temp==rev):
    print("This value is Palindrome Number")
else:
    print("This Value is not a Palindrome Number")
