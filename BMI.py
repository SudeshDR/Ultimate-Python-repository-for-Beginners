height=float(input("Enter the height in cm:"))
weight=float(input("Enter the weight iin kg:"))
bmi=weight/(height/100)**2
print("Your body mass Index is",bmi)
if bmi<=18.5:
    print("OOPS,you are underweight")
elif bmi<=24.9:
    print("Awesome you are healthy")
elif bmi<=29.9:
    print("You are over-weight")
else:
    print("Sheeshhh!you are OBESE")
