#PASSWORD GENERATOR IN PYTHON

import string
import random
#getting password length
length=int(input("Enter the length of the password: "))
print('''Choose what characters you need in the password:
           1.Digits
           2.Numbers
           3.Special Characters
           4.Exit''')
characterlist=" "

#Getting character set for password
while(True):
    choice=int(input("Pick a Number: "))
    if(choice==1):
        #adding letters to pssword
        characterlist+=string.ascii_letters
    elif(choice==2):
        #adding digits to password
        characterlist+=string.digits
    elif(choice==3):
        #adding special characters to password
        characterlist+=string.punctuation
    elif(choice==4):
        break
    else:
        print("Please pick a valid option")

password= [ ]
for i in range(length):
    #picking a random character in our character list
    randomchar= random.choice(characterlist)
    #appending a random character to password
    password.append(randomchar)
#printing the password as a string
print("The random password is: "+" ".join(password))
      
