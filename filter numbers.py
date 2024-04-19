#Filtering even numbers

numbers=[1,2,3,4,5,6,7,8,9,0]
even=[num for num in numbers if num%2==0]
print(f"Even:"{even})

odd=[num for num in numbers if num%2!=0]
print(f"Odd:"{odd})
