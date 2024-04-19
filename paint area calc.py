roomwidth=0
roomheight=0
roomtotal=0
roompaint=0
roomwidth=float(input("Enter the room width::"))
roomheight=float(input("Enter the room height::"))
roomtotal=((roomwidth+roomheight)*4)
paintselection=str(input("Please choose a selection of paint : Luxury, Standard or Economy::"))
if paintselection=="Luxury":
    roompaint=roomtotal*1.45
elif paintselection=="Standard":
    roompaint=roomtotal*1.00
elif paintselection=="Economy":
    roompaint=roomtotal*0.45
undercoat=str(input("Would you like to use an undercoat? Y/N:"))
if undercoat=="Y":
    undercoating=(roomtotal*0.5)
elif undercoat=="N":
    undercoating=0
totalcost=roompaint+undercoating
print("The total cost of painting this room is $", totalcost)
    
