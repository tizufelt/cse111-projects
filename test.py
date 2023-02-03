

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



students = {
    "10-450-1203": "Jorge Soares",
    "75-421-2310": "Abdul Ali",
    "07-103-5621": "Michelle Davis"
}

students["81-298-9238"] = "Sama Patel"

