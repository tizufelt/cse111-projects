import math

num_items = int(input("Enter the number of items: "))
item_perbox = int(input("Enter the number of items per box: "))

box = math.ceil(num_items / item_perbox)
print()

print(f"For {num_items} items, packing {item_perbox} items in each box, you will need {box} boxes")
