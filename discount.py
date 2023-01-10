from datetime import datetime

discount = 0.10
salestax_rate = 0.06

subtotal = float(input("Please enter the subtotal: "))

current_DT = datetime.now()

weekday = current_DT.weekday()

if subtotal >= 50 and (weekday == 1 or weekday == 2):
    discount = round(subtotal * discount, 2)
    print(f"Discount amount: {discount:.2f}")
    subtotal -= discount
    
salestax = round(subtotal * salestax_rate, 2)
print(f"Sales tax amount: {salestax:.2f}")

total = subtotal + salestax

print(f"Total: {total:.2f}")
    




