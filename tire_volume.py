import math

print()
width = int(input(" Enter the width of the tire in mm (example: 205):"))
ratio = int(input(" Enter the aspect ratio of the tire (example: 55): "))
diameter = int(input(" Enter the diameter of the tire (example: 18):"))
pi = math.pi

print()
volume=(pi * (pow(width,2)*ratio*(width*ratio+2540*diameter)))/10000000000

print(f"the approximate volume is {volume:.2f} liters")
print()

