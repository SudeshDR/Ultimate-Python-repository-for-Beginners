print("Welcme to the Tip Calculator")
bill=float(input("What was the total bill?$"))
tip=int(input("How much tip would you like to give ?"))
people=int(input("How many people to split the bill into?"))
tip_as_percent=tip/100
total_tip=bill*tip_as_percent
total_bill=bill+total_tip
bill_perhead=total_bill/people
final_amt=round(bill_perhead,2)
print(f"Each person should pay:${final_amt}")
