

"""
I = [1, 2, 3]
I_iter = iter(I)

while True:
    item = next(I_iter, "end")
    if item == "end":
        break
    print(item)
"""

"""
b = [1,2,3,4,5,6,7]
a = iter(b)
for x in a :
    if (x % 2) == 0 :
        print(next(a))
"""


cats = []
for x in range(3):
    cats.append(input("enter in a cat name..."))

print(cats)


