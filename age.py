import datetime

def calculate(birth_year):
    current_year=datetime.date.today().year
    age=current_year-birth_year
    return age

birth_year=int(input("Enter your Birth year: "))
age=calculate(birth_year)
print("Your age is ",age)
