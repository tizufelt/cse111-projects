import math
from datetime import datetime

date = datetime.today().strftime("%Y-%m-%d")




print()
width = int(input(" Enter the width of the tire in mm (example: 205):"))
ratio = int(input(" Enter the aspect ratio of the tire (example: 55): "))
diameter = int(input(" Enter the diameter of the tire (example: 18):"))
pi = math.pi

print()
volume=(pi * (pow(width,2)*ratio*(width*ratio+2540*diameter)))/10000000000

print(f"the approximate volume is {volume:.2f} liters")
print()

#SECTION FOR EXTRA PIECE THAT ASKS FOR NUMBER AND STORES IT TO THE TEXT FILE
interested = input("Are you intereded in purchasing these size tires?: y or n ")

if interested == "y":
    number = input("Please enter you a contact number: ")
    print()
    print("Someone will contact you shortly to help you with your purchase, Thank You. ")
    print()
    
else:
    number = "blank"
    print(" Thank you for your time.")
    print()
   
# Section for TEXT File writing appending       
newvolume = round(volume, 2)
file = open("volumes.txt", "a")
alist = [date + ", ", str(width) + ", ", str(ratio) + ", ", str(diameter) + ", ", str(newvolume) + ", ", str(number), "\n"]
file.writelines(alist)
file.close()

